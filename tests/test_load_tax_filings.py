import unittest
from unittest.mock import patch, MagicMock

from src.load_tax_filings import load_filings_to_postgres


class TestLoadTaxFilings(unittest.TestCase):
    def test_loads_filings_to_postgres(self):
        filings = [
        {
            "filing_id": "11111111-1111-1111-1111-111111111111",
            "taxpayer_id": "SYN-TP-1001",
            "tax_type": "VAT",
            "filing_period": "2026-08",
            "county": "Nairobi",
            "declared_tax_amount": 5000.00,
            "payment_status": "PAID",
            "submitted_at": "2026-08-22T08:00:00+03:00",
        }]
        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        with patch("src.load_tax_filings.connect_to_database")  as mock_connect:
            mock_connect.return_value.__enter__.return_value = mock_connection
            loaded_count = load_filings_to_postgres(filings)
            self.assertEqual(loaded_count, 1)

    def test_returns_zero_when_filing_already_exists(self):
        filings = [{
            "filing_id":"11111111-1111-1111-1111-111111111111",
            "taxpayer_id":"SYN-TP-1001",
            "tax_type":"VAT",
            "filing_period":"2026-08",
            "county":"Nairobi",
            "declared_tax_amount":5000.00,
            "payment_status":"PAID",
            "submitted_at":"2026-08-22T08:00:00+03:00",
            }]

        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 0

        with patch("src.load_tax_filings.connect_to_database") as mock_connect:
            mock_connect.return_value.__enter__.return_value = mock_connection
            loaded_count = load_filings_to_postgres(filings)
        self.assertEqual(loaded_count, 0)
