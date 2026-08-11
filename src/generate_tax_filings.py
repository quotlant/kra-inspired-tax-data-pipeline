#Generate synthetic tax filings 

from datetime import datetime, timezone
from random import choice, randint, uniform 
from uuid import uuid4
import json 
from pathlib import Path




TAX_TYPES = ("VAT", "PAYE", "INCOME_TAX")
PAYMENT_STATUSES = ("PAID", "PENDING", "OVERDUE")
COUNTIES = ("Nairobi", "Mombasa", "Kisumu", "Nakuru", "Uasin Gishu")

#return one valid synthetic tax-filing-record
def generate_valid_filing() -> dict[str, str | float]:


    return {
        "filing_id": str(uuid4()),
        "taxpayer_id": f"SYN-TP-{randint(1, 999999):06d}",
        "tax_type": choice(TAX_TYPES),
        "filing_period": "2026-07",
        "county": choice(COUNTIES),
        "declared_tax_amount": round(uniform(1_000, 500_000), 2),
        "payment_status": choice(PAYMENT_STATUSES),
        "submitted_at": datetime.now(timezone.utc).isoformat(), # Use UTC so timestamps remain consistent across environments.
    
    }
    

#return 'count' indepedently generated valid filing records  
def generate_valid_filings(count: int) -> list[dict[str,str | float]]:
    return [generate_valid_filing() for _ in range(count)]
    

#write filings to a JSONL file, one JSON object per line
def write_filings_to_jsonl(
    filings: list[dict[str, str | float]], output_path: Path
) -> None:
    with output_path.open("w", encoding="utf-8") as file:
        for filing in filings:
            file.write(json.dumps(filing) + "\n") #a new line after each object preserves the JSONL format



# Local development entry point; Airflow will later orchestrate these functions.
if __name__ == "__main__":
    #print(generate_valid_filings(3))
    filings = generate_valid_filings(3)
    output_path = Path("data/raw/synthetic_tax_filings.jsonl")
    
    write_filings_to_jsonl(filings, output_path)
    print(f"Wrote {len(filings)} filings to {output_path}")