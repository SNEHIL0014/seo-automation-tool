
# Technical Specifications for Car Rental Architecture

## 1. System Architecture
- **Frontend:** React with Tailwind CSS
- **Backend:** Node.js/Python FastAPI
- **Database:** PostgreSQL for persistent data, Redis for caching.

## 2. Logic Workflow (Insurance Verification)
1. User uploads document.
2. System extracts data using OCR.
3. System pings Insurance Verification API.
4. If valid, 'RentalStatus' is set to 'Verified'.
    