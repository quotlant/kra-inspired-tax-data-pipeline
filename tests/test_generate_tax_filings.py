import unittest
from src.generate_tax_filings import generate_valid_filing




class TestGenerateTaxFilings (unittest.TestCase):
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
        
        
        