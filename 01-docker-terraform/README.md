# Module 1 — Docker + Terraform

Course units: `01-docker-terraform/01-introduction.md` → `13-gcp-overview.md`
Homework: `cohorts/2026/01-docker-terraform/homework.md`

## Build checklist

- [ ] `pipeline/ingest_data.py` loads one month of yellow taxi data into Postgres in chunks (unit 06)
- [ ] `pipeline/docker-compose.yaml` runs Postgres + pgAdmin; pgAdmin connects to Postgres (units 07, 09)
- [ ] `pipeline/Dockerfile` packages the script; it runs on the Compose network (unit 08)
- [ ] Also load the taxi zone lookup table
- [ ] `terraform/` creates a GCS bucket + BigQuery dataset, with variables (units 12–13)

## Run

```bash
cd pipeline
docker compose up -d
uv run python ingest_data.py --year 2021 --month 1
```

## Homework answers

| Q | Answer | How I got it |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |

## What would break this in production?

-
-
-
