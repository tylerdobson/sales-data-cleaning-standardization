# Architecture

```mermaid
flowchart LR
  A[Real Online Retail II CSV] --> B[Process script]
  B --> C[Cleaned CSV]
  B --> D[Rejected CSV]
  B --> E[SQLite audit mart]
  B --> F[Audit JSON]
  F --> G[Proof images]
  C --> H[Portfolio-ready analysis]
  D --> H
  E --> H
  G --> H
```

## Design choices

- Keep the pipeline script-first so it is reproducible without notebooks.
- Store rejected rows instead of discarding them so the audit trail is visible.
- Generate proof images directly from the computed summary so the visuals cannot drift away from the numbers.
- Keep the bundled SQLite file compact and reviewable rather than shipping a giant binary artifact.
