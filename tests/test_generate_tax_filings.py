import unittest
from src.generate_tax_filings import generate_valid_filing, generate_valid_filings




class TestGenerateTaxFilings(unittest.TestCase):
    def test_record_has_all_contract_fields(self) -> None:
        record = generate_valid_filing()
        
        expected_fields = {
            
        "filing_id",
        "taxpayer_id",
        "tax_type",
        "filing_period",
        "county",
        "declared_tax_amount",
        "payment_status",
        "submitted_at",
    
        }
        
        self.assertEqual(set(record), expected_fields) 
        
        
    def test_generates_requested_number_of_filings(self) -> None:
        filings = generate_valid_filings(3)
        
        self.assertEqual(len(filings), 3)
        
        
        
        
        