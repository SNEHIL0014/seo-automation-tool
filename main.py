import requests
from bs4 import BeautifulSoup
import json
import time
from google.genai import Client

# Initialize Client
client = Client(api_key="AIzaSyBWniRbxpo9CiQQXuaDeto1JizGKM3OW28")

def scrape_product(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True)
        return {"title": title}
    except:
        print("⚠️ Note: Extracting info from URL structure...")
        # Fixed logic: Find the actual words in the eBay link
        if "itm/" in url:
            # Get the part after 'itm/' and before the '/' or '?'
            url_segment = url.split("itm/")[1].split("?")[0].split("/")[0]
            # If it's just a number, the name is usually in the next part of the URL
            if url_segment.replace(".","").isdigit():
                 url_segment = "Product" 
            name = url_segment.replace("-", " ").title()
            return {"title": name}
        return {"title": "Premium Laptop"}

def get_seo_keywords(title):
    query = " ".join(title.split()[:3])
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    try:
        res = requests.get(url, timeout=5)
        kws = json.loads(res.text)[1][:4]
        return kws if kws else ["best price", "features", "review"]
    except:
        return ["best price", "features", "review"]

def generate_blog_with_gemini(data, keywords):
    title = data['title']
    kw_str = ", ".join(keywords)
    prompt = f"Write a professional 200-word SEO blog post for: {title}. Keywords: {kw_str}. Use Markdown headers."
    
    try:
        # PERMANENT FIX: Using 'gemini-1.5-flash' with the client.models structure
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Generation Error: {e}"

if __name__ == "__main__":
    print("🚀 Running AI Automation Pipeline...")
    product_url = input("Enter Product URL: ")
    
    data = scrape_product(product_url)
    print(f"✅ Product Identified: {data['title']}")

    kws = get_seo_keywords(data['title'])
    print(f"✅ Keywords: {kws}")

    print("\nStep 3: Generating AI Content...")
    # Quota safety wait
    time.sleep(2) 
    
    final_blog = generate_blog_with_gemini(data, kws)
    
    with open("SEO_Blog_Post.md", "w", encoding="utf-8") as f:
        f.write(final_blog)
    
    print("\n--- 📄 GENERATED BLOG ---")
    print(final_blog)
    print("\n✅ Success! File saved as 'SEO_Blog_Post.md'")