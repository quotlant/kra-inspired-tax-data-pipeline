import unittest
import tempfile
from pathlib import Path

from src.generate_tax_filings import (
    generate_valid_filing,
    generate_valid_filings, 
    write_filings_to_jsonl
)
from src.process_tax_filings import (
    read_filings_from_jsonl,
    process_filings_from_jsonl,
)


class TestProcessTaxFilings(unittest.TestCase):
    def test_reads_filings_from_jsonl(self)-> None:
        expected_filings = generate_valid_filings(2)
        
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "filings.jsonl"
            write_filings_to_jsonl(expected_filings, input_path)
            
            actual_filings = read_filings_from_jsonl(input_path)
            
        self.assertEqual(actual_filings, expected_filings)
        
        
    def test_process_valid_and_rejected_filings(self) -> None:
        valid_filing = generate_valid_filing()
        invalid_filing = generate_valid_filing()
        invalid_filing["tax_type"] = "EXCISE_DUTY"
        
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "filings.jsonl"
            write_filings_to_jsonl(
                [valid_filing, invalid_filing],
                input_path,
            )
            
            valid_filings, rejected_filings = process_filings_from_jsonl(
                input_path
            )
            
            self.assertEqual(valid_filings, [valid_filing])
            self.assertEqual(rejected_filings[0]["filing"], invalid_filing)
            