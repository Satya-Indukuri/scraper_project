import requests

def fetch_url(url, timeout=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (JobMonitorBot/1.0; +https://example.com)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status() # raises HTTPError if not 200
        print(f"[INFO] Fetched {url}: ({response.status_code})")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# html = fetch_url("https://quotes.toscrape.com")
# print(html[0:500])