import os

import psycopg
from dotenv import load_dotenv
from pathlib import Path
from src.process_tax_filings import read_filings_from_jsonl

load_dotenv()

INSERT_FILING_SQL = """
INSERT INTO tax_filings(
filing_id,
taxpayer_id,
tax_type,
filing_period,
county,
declared_tax_amount,
payment_status,
submitted_at
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s )
ON CONFLICT (filing_id) DO NOTHING;

"""



def connect_to_database():
    return psycopg.connect(
host=os.environ["POSTGRES_HOST"],
port=os.environ["POSTGRES_PORT"],
dbname=os.environ["POSTGRES_DB"],
user=os.environ["POSTGRES_USER"],
password=os.environ["POSTGRES_PASSWORD"],
)

def load_filings_to_postgres(filings: list[dict[str, object]]) -> int:
    inserted_count = 0
    with connect_to_database() as connection:
        with connection.cursor() as cursor:
            for filing in filings:
                values = (
                    filing["filing_id"],
                    filing["taxpayer_id"],
                    filing["tax_type"],
                    filing["filing_period"],
                    filing["county"],
                    filing["declared_tax_amount"],
                    filing["payment_status"],
                    filing["submitted_at"],
                )
                cursor.execute(INSERT_FILING_SQL, values)
                inserted_count += cursor.rowcount
    return inserted_count


if __name__ == "__main__":
    input_path = Path("data/processed/valid_filings.jsonl")
    filings = read_filings_from_jsonl(input_path)
    loaded_filings = load_filings_to_postgres(filings)
    print(f"Loaded {loaded_filings} new filings into PostgreSQL")