import requests
from bs4 import BeautifulSoup
import time

def scrape_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    
    # Try up to 3 times if there is a timeout
    for attempt in range(3):
        try:
            # Increased timeout to 15 seconds
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Improved selectors for eBay
            title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No Title Found"
            
            # eBay specific description search
            description_tag = soup.find('meta', attrs={'name': 'description'})
            description = description_tag['content'] if description_tag else "No Description Found"
            
            return {"title": title, "description": description[:500]}

        except (requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
            print(f"Attempt {attempt + 1} failed... retrying.")
            time.sleep(2) # Wait 2 seconds before retrying
            if attempt == 2:
                return {"error": "Site is taking too long to respond. Try a different URL."}

if __name__ == "__main__":
    test_url = "https://www.ebay.com/itm/335762770305" 
    data = scrape_product(test_url)
    print(data)