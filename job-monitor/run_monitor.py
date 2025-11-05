from src.utils import fetch_url
from src.scrapers.quotes_scraper import parse
from src.storage.csv_storage import CSVStorage
from src.storage.db_storage import DBStorage

def main():
    url = "https://quotes.toscrape.com"
    html = fetch_url(url)
    if not html:
        print("[ERROR] Could not fetch page.")
        return
    
    jobs = parse(html)
    storage = CSVStorage("data/jobs.csv")
    storage.save(jobs)

    dbstorage = DBStorage("data/jobs.db")
    dbstorage.save_jobs(jobs)

    print(dbstorage.get_all_jobs())

    print(f"[SUCCESS] Completed scraping from {url}")

if __name__ == "__main__":
    main()
