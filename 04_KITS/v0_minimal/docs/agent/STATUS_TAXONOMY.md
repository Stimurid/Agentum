# STATUS_TAXONOMY

Allowed final statuses:

- done
- partial
- blocked
- needs-review
- unsafe-without-preflight
- insufficient-context

Rules:

- done requires evidence
- partial is better than fake done
- blocked is valid when the next safe step needs external input or approval
- never hide failure behind optimistic narration or silent fallback
