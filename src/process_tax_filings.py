"""process raw synthetic tax filings"""

import json
from pathlib import Path

from src.validate_tax_filings import (
    split_filings_by_validity,
)

from src.generate_tax_filings import write_filings_to_jsonl


def read_filings_from_jsonl(input_path: Path) -> list[dict[str, object]]:
    
    """read non-empty JSONL lines into filing dictionaries"""
    
    with input_path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]
    
    
def process_filings_from_jsonl(
    input_path: Path
) -> tuple[list[dict[str,object]], list[dict[str, object]]]:
    """read a jsonl batch and split it into valid and rejected filings"""
    filings = read_filings_from_jsonl(input_path)
    
    return split_filings_by_validity(filings)    
    
    
def process_and_write_filings(
    input_path: Path,
    valid_output_path: Path,
    rejected_output_path: Path,
) -> tuple[list[dict[str,object]], list[dict[str,object]]]:
    valid_filings, rejected_filings = process_filings_from_jsonl(input_path)
 
    
    write_filings_to_jsonl(valid_filings, valid_output_path)
    write_filings_to_jsonl(rejected_filings, rejected_output_path)
    
    return valid_filings, rejected_filings
    
    
if __name__ == "__main__":
    input_path = Path("data/raw/synthetic_tax_filings.jsonl")
    valid_output_path = Path("data/processed/valid_filings.jsonl")
    rejected_output_path = Path("data/processed/rejected_filings.jsonl")
    
    valid_filings, rejected_filings = process_and_write_filings(
        input_path,
        valid_output_path,
        rejected_output_path
    )
    
    print(f"Wrote {len(valid_filings)} valid filings to {valid_output_path}")
    print(f"Wrote {len(rejected_filings)} rejected filings to {rejected_output_path}")