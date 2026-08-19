"""process raw synthetic tax filings"""

import json
from pathlib import Path

from src.validate_tax_filings import (
    split_filings_by_validity,
)


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
    