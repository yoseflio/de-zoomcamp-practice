# Course reference: 01-docker-terraform/03-dockerizing-pipeline.md, 08-dockerizing-ingestion.md
FROM python:3.13-slim

# TODO: copy the uv binary in (COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/)
# TODO: set WORKDIR and put the project's .venv/bin on PATH
# TODO: copy pyproject.toml, .python-version, uv.lock first, then `uv sync --locked`
#       (why before the script? think about layer caching)
# TODO: copy ingest_data.py and set ENTRYPOINT
