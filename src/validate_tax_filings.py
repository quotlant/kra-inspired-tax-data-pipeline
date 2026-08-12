#validate synthetic tax filings

from src.generate_tax_filings import TAX_TYPES


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
        
    return errors

