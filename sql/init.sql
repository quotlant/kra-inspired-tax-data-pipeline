CREATE TABLE tax_filings (
    filing_id UUID PRIMARY KEY,
    taxpayer_id TEXT NOT NULL,
    tax_type TEXT NOT NULL CHECK (tax_type IN ('VAT','PAYE', 'INCOME_TAX')),
    filing_period TEXT NOT NULL,
    county TEXT NOT NULL,
    declared_tax_amount NUMERIC(14, 2) NOT NULL CHECK (declared_tax_amount > 0),
    payment_status TEXT NOT NULL CHECK (payment_status in ('PAID', 'PENDING', 'OVERDUE')),
    submitted_at TIMESTAMPTZ NOT NULL, 
    loaded_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);