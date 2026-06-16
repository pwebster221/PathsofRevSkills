from __future__ import annotations
import os
import subprocess


class MintError(RuntimeError):
    """Raised when generate_jwt.py fails to mint a token."""


def mint_peer_token(honcho_repo_path: str, workspace_id: str, peer_id: str, runner=subprocess.run) -> str:
    script = os.path.join("scripts", "generate_jwt.py")
    cmd = ["python", script, "--workspace", workspace_id, "--peer", peer_id, "--print-only"]
    result = runner(cmd, cwd=honcho_repo_path, capture_output=True, text=True)
    if result.returncode != 0:
        raise MintError(f"generate_jwt.py failed for peer '{peer_id}': {(result.stderr or '').strip()}")
    return result.stdout.strip()
