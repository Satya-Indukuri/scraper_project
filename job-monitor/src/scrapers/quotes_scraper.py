from bs4 import BeautifulSoup
from src.utils import fetch_url

def parse(html, base_url="https://quotes.toscrape.com"):
    soup = BeautifulSoup(html, 'lxml')
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        quote_text = q.find("span", class_="text").get_text(strip = True)
        quote_author = q.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]

        quotes_data.append({
            "title":quote_text,         # maps to job title later 
            "company":quote_author,     # maps to company later
            "location":",".join(tags),  # demo: tags as location
            "url":base_url,
            "posted_date":None,
            "source":"quotes.toscrape.com"
        })

    print(f"[INFO] Parsed {len(quotes_data)} quotes")
    return quotes_data

# html = fetch_url("https://quotes.toscrape.com")
# data = parse(html)
# print(data)