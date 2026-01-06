import os

def generate_specs_offline(requirement):
    """Simulates an AI response so you can test your pipeline without an API key."""
    print("🔄 Running in Offline Mode (No API required)...")
    mock_response = f"""
# Technical Specifications for {requirement}

## 1. System Architecture
- **Frontend:** React with Tailwind CSS
- **Backend:** Node.js/Python FastAPI
- **Database:** PostgreSQL for persistent data, Redis for caching.

## 2. Logic Workflow (Insurance Verification)
1. User uploads document.
2. System extracts data using OCR.
3. System pings Insurance Verification API.
4. If valid, 'RentalStatus' is set to 'Verified'.
    """
    return mock_response

if __name__ == "__main__":
    biz_idea = input("Enter Business Requirement: ")
    specs = generate_specs_offline(biz_idea)
    
    with open("Technical_Specs.md", "w", encoding="utf-8") as f:
        f.write(specs)
    
    print("\n✅ Success! Saved to 'Technical_Specs.md' (Offline)")