# Transit Overlay Fallback

Use this when a Kairos transit overlay succeeds but is response-cap trimmed before the transit-to-natal contact list appears, or when the full endpoint rejects a timestamp shape.

## Retry sequence

1. Normalize the target moment to UTC ISO-8601 (`YYYY-MM-DDTHH:MM:SSZ`).
2. For an inline natal payload, use the documented `chart_input.birth_data` shape and include the anonymous/linkage flag expected by the endpoint.
3. If the overlay remains too large, call the current-transit endpoint for the observer's present location and preserve its timestamp.
4. Extract natal and transit ecliptic longitudes.
5. Compute each separation as:

   `d = abs((transit_lon - natal_lon + 180) % 360 - 180)`

6. Compare `d` with the intended aspect angles: 0, 60, 90, 120, 150, and 180 degrees. The orb is `abs(d - aspect_angle)`.
7. Apply the reading's declared orb policy consistently. Prefer tight outer-planet contacts; do not widen an orb merely to create another Trial.
8. Record exact longitudes, separation, and orb in working notes before writing mythic prose.

## Boundaries

- This reconstructs geometry only. It does not reconstruct applying/separating status unless speeds and relative motion are also evaluated.
- A sign relationship is a sanity check, not proof of an aspect.
- Distinguish a successful but truncated overlay from a failed computation. Never describe the transit endpoint as generally unavailable.
- If the reading uses relocated houses, use the observer location for transit cusps while keeping natal houses tied to the birth location.

## Verification

For every narrated Trial, independently confirm that the stated aspect angle plus/minus the stated orb equals the computed angular separation. Include only contacts that pass the chosen orb policy.
