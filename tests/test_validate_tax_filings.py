import unittest
from src.generate_tax_filings import generate_valid_filing
from src.validate_tax_filings import validate_filing



class TestValidateTaxFilings(unittest.TestCase):
    def test_rejects_unsupported_tax_type(self) -> None:
        filing = generate_valid_filing()
        filing["tax_type"] = "EXCISE_DUTY"
        
        errors = validate_filing(filing)
        
        self.assertIn("Unsupported tax type", errors)
        
        
    def test_rejects_non_positive_tax_amount(self) -> None:
        filing = generate_valid_filing()
        filing["declared_tax_amount"] = -100.0
        
        errors = validate_filing(filing)
        
        self.assertIn("Declared tax amount must be positive", errors)
        
        
    def test_rejects_invalid_taxpayer_id(self) -> None:
        filing = generate_valid_filing()
        filing["taxpayer_id"] = ""
        
        errors = validate_filing(filing)
        
        self.assertIn("Taxpayer ID must use the SYN-TP- prefix", errors)
        
    def test_rejects_invalid_filing_period(self) -> None:
        filing = generate_valid_filing()
        filing["filing_period"] = "2026-13"
        
        errors = validate_filing(filing)
        
        self.assertIn("Filing period must use YYYY-MM format", errors)
        
        
    def test_accepts_valid_filing(self) -> None:
        filing = generate_valid_filing()
        
        errors = validate_filing(filing)
        
        self.assertEqual(errors, [])
        