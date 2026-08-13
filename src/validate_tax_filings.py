#validate synthetic tax filings

from src.generate_tax_filings import TAX_TYPES
from datetime import datetime


def validate_filing(filing: dict[str, object]) -> list[str]:
    """return validation error message for one synthetic tax filing"""
    errors: list[str] = []
    
    if filing.get("tax_type") not in TAX_TYPES:
        errors.append("Unsupported tax type")
        



    if (
        not isinstance(filing.get("declared_tax_amount"), (int, float))
        or filing["declared_tax_amount"] <= 0
    ):
        errors.append("Declared tax amount must be positive")
        
    if (
        not isinstance(filing.get("taxpayer_id"), str)
        or not filing["taxpayer_id"].startswith("SYN-TP-")
    ):
        errors.append("Taxpayer ID must use the SYN-TP- prefix")
        
    filing_period = filing.get("filing_period")
    
    if not isinstance(filing_period, str):
        errors.append("Filing period must use YYYY-MM format")
    else:
        try:
            datetime.strptime(filing_period, "%Y-%m")
        except ValueError:
            errors.append("Filing period must use YYYY-MM format")
        
   
        
    return errors

