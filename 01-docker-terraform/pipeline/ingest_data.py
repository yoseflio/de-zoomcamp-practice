"""Ingest one month of NYC yellow taxi data into PostgreSQL.

Course reference: 01-docker-terraform/05-data-ingestion.md, 06-ingestion-script.md
Data: https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_{YYYY}-{MM}.csv.gz
"""

import click


@click.command()
@click.option("--pg-user", default="root")
@click.option("--pg-pass", default="root")
@click.option("--pg-host", default="localhost")
@click.option("--pg-port", default=5432, type=int)
@click.option("--pg-db", default="ny_taxi")
@click.option("--year", default=2021, type=int)
@click.option("--month", default=1, type=int)
@click.option("--target-table", default="yellow_taxi_data")
@click.option("--chunksize", default=100_000, type=int)
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table, chunksize):
    # TODO 1: build the download URL from year/month.
    # TODO 2: create a SQLAlchemy engine — URL scheme is postgresql+psycopg:// (psycopg 3).
    # TODO 3: read the CSV with pandas in chunks (iterator=True, chunksize=...),
    #         with explicit dtypes and parse_dates for the pickup/dropoff columns.
    # TODO 4: on the first chunk, create the table (df.head(0).to_sql(..., if_exists="replace")).
    # TODO 5: append every chunk; show progress with tqdm.
    # Stretch: make re-runs idempotent, and log rows loaded vs. rows expected.
    raise NotImplementedError


if __name__ == "__main__":
    run()
