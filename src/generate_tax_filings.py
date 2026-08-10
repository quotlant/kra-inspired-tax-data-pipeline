from datetime import datetime, timezone
from random import choice, randint, uniform 
from uuid import uuid4



TAX_TYPES = ("VAT", "PAYE", "INCOME_TAX")
PAYMENT_STATUSES = ("PAID", "PENDING", "OVERDUE")
COUNTIES = ("Nairobi", "Mombasa", "Kisumu", "Nakuru", "Uasin Gishu")

def generate_valid_filing() -> dict[str, str | float]:
    
    return {
        "filing_id": str(uuid4()),
        "taxpayer_id": f"SYN-TP-{randint(1, 999999):06d}",
        "tax_type": choice(TAX_TYPES),
        "filing_period": "2026-07",
        "county": choice(COUNTIES),
        "declared_tax_amount": round(uniform(1_000, 500_000), 2),
        "payment_status": choice(PAYMENT_STATUSES),
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    
    }
    




if __name__ == "__main__":
    print(generate_valid_filing())