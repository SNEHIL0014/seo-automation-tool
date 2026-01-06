🚀 AI Multi-Tool Suite: SEO & Architecture 🏗️
A powerful Python-based automation suite leveraging the Google Gemini 2.0/1.5 Flash SDK to automate technical design and digital marketing workflows.

---

📂 Repository Modules
1. SEO Content Automation Tool
Purpose: Scrapes product data and generates high-ranking marketing copy.

Workflow: 1. Extracts product titles (eBay optimized) using BeautifulSoup4. 2. Identifies trending terms via Google Suggest API. 3. Generates 200-word SEO-optimized blog posts.

Output: SEO_Blog_Post.md

2. AI Architecture Pipeline
   
Purpose: Converts business requirements into Senior-level technical blueprints.

Workflow:

Analyzes requirements for System Architecture and Data Models.

Generates SQL Schemas and Logic Flowcharts.

Includes a Resilience Engine with exponential backoff for API stability.

Output: Technical_Specs.md

---

🛠️ Technical Stack
Language: Python 3.13+

AI Models: Gemini 2.0 Flash (Architecture) & Gemini 1.5 Flash (SEO)

SDK: google-genai (Modern 2026 Standard)

Libraries: BeautifulSoup4, Requests, python-dotenv

---

📋 Installation & Setup
Clone & Navigate:

PowerShell

git clone https://github.com/SNEHIL0014/seo-automation-tool.git

cd seo-automation-tool

Environment Setup:

PowerShell

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install google-genai beautifulsoup4 requests

API Key Configuration: Ensure your API Key is set in the script variables or as an environment variable.

---

🖥️ Usage

To run the SEO Tool:

PowerShell

python main.py

To run the Architecture Tool:

PowerShell

python architecture_tool.py
