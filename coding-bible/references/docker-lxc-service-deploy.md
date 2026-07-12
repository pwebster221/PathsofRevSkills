# Editing & deploying a Dockerized service inside a Proxmox LXC

Worked pattern for safely changing code in a containerized FastAPI service that
runs as a Docker Compose stack *inside* an LXC (e.g. DailyAPICall / Mercury on
CT 520). The host's file/patch tools operate on the **Proxmox host filesystem**,
but the service code lives **inside the LXC** and is **baked into the image at
build time** (Dockerfile `COPY . .`), so neither host edits nor a bare restart
suffice. This is the load-bearing loop.

## The edit → deploy → verify loop

1. **Pull the files to the host to edit precisely.** Host `read_file`/`patch`
   can't see inside the container's image layers. Pull each target file out:
   ```
   pct pull <vmid> /opt/<Service>/src/foo.py /tmp/<svc>-edit/src/foo.py
   ```
   Edit on the host with `patch`/`write_file` (gets you fuzzy-match + lint +
   diff). Byte-compile locally before pushing: `python3 -m py_compile <files>`.

2. **Back up in-container before overwriting.** Timestamp tag so rollback is
   trivial:
   ```
   pct exec <vmid> -- bash -c 'cd /opt/<Service> && for f in main.py src/x.py; \
     do cp -av $f _backups/$(echo $f | tr / _).$(date +%Y%m%d-%H%M%S); done'
   ```

3. **Push back + restore ownership/perms.** `pct push` lands files as root with
   default perms; match the originals (commonly `root:root 664` in these repos):
   ```
   pct push <vmid> /tmp/<svc>-edit/src/foo.py /opt/<Service>/src/foo.py
   pct exec <vmid> -- bash -c 'chown root:root <files>; chmod 664 <files>'
   ```

4. **Code baked into the image ⇒ REBUILD, not restart.** A `docker compose
   restart` reruns the *old* image. You must rebuild:
   ```
   pct exec <vmid> -- bash -c 'cd /opt/<Service> && docker compose build app'
   ```
   Builds reliably exceed the foreground command window — run in **background
   with notify_on_complete**, then `process wait`/`poll`. The container's login
   MOTD (fastfetch/ProxMenux banner) pollutes the captured stdout; the real
   build result is at the very tail (`naming to docker.io/...:latest`,
   `Built`). Don't mistake the banner for the build output.

5. **⚠️ VERIFY THE IMAGE ACTUALLY GOT THE CODE — do not trust the build log.**
   BuildKit's output ordering can show `CACHED` next to `COPY . .` even when the
   new files ARE in the layer. Confirm by reading the file *out of the freshly
   built image* via a throwaway container, BEFORE recreating the live one:
   ```
   docker run --rm --entrypoint cat <image>:latest /app/src/foo.py | grep <sentinel>
   docker run --rm --entrypoint python <image>:latest -c "import newdep; print(newdep.__version__)"
   ```
   This caught a near-miss twice — treat it as mandatory, not optional.

6. **Recreate the live container from the new image.**
   ```
   pct exec <vmid> -- bash -c 'cd /opt/<Service> && docker compose up -d app'
   ```
   Wait out the healthcheck `start_period`, then verify health + the specific
   behavior you changed.

## Running tests / a real probe without a full rebuild

The runtime image usually has pytest. To iterate fast, `docker cp` the new
source + tests into the *running* container and run pytest via `docker exec -w
/app`:
```
docker cp /opt/<Service>/src/news/foo.py <container>:/app/src/news/foo.py
docker exec -w /app <container> python -m pytest tests/test_foo.py -v
```
If a test needs a new dependency that isn't in the current image yet, install it
**ephemerally** for the test pass (`docker exec <container> pip install --quiet
<pkg>`), knowing the durable install comes via the rebuild's requirements.txt.
This lets you green the tests AND run a real end-to-end probe before paying for
the rebuild.

## Verifying side-effecting writes (Mongo/Neo4j) — read them back

A pipeline returning `success=True` is a self-report. For any run that writes to
a datastore, confirm persistence independently: query the collection/graph back
(`count_documents`, an aggregate for the shape you expect, a sample doc). The
write path is only proven when you've read the data back, not when the function
returned cleanly. (Same discipline the delegation/verification rules demand.)

## Feature-flag new pipelines OFF by default

When adding a second pipeline / scheduled job into a live service, gate it behind
a settings flag defaulting to `False`, and prove the gate BOTH directions:
flag-off → the new jobs are absent from the scheduler; flag-on (test via an
ephemeral env override on a throwaway `docker run`, not by editing live `.env`)
→ jobs register at the right triggers. Deploying inert code carries near-zero
risk to the running service; flipping it on becomes a deliberate, separate step.

## Soft vs hard dependencies in multi-source collectors

External sources WILL fail intermittently (observed in one run: a feed returning
0 items, another 403 to the default UA, a public API 429 rate-limiting). Design
each non-critical source to return empty + log on ANY failure so one bad source
never sinks the run; reserve hard-fail for the stages that must succeed
(collect-produced-something, normalize, store). Verify this resilience in the
wild — a run that survives real partial failures is the proof, not the unit test.

## Pitfalls recap

- Host patch tools edit the HOST fs; service code is INSIDE the LXC + image. Pull/push.
- `docker compose restart` ≠ picking up code changes. Rebuild.
- BuildKit `CACHED` on `COPY` can lie — verify file content inside the built image.
- MOTD banner pollutes `docker compose build` stdout; read the tail.
- Restore `chown root:root` + `chmod 664` after `pct push`.
- Don't restart/rebuild mid-run: check the scheduler's last/next run first; pick a window.
