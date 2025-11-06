from src.utils import fetch_url
from src.scrapers.remoteok_scraper import parse_remoteok_jobs
from src.storage.csv_storage import CSVStorage
from src.storage.db_storage import DBStorage

def main():
    url = "https://remoteok.com/"
    html = fetch_url(url)
    if not html:
        print("[ERROR] Could not fetch page.")
        return

    jobs = parse_remoteok_jobs()
    if not jobs:
        print("[WARN] No jobs parsed.")
        return
    storage = CSVStorage("data/jobs.csv")
    storage.save(jobs)

    dbstorage = DBStorage("data/jobs.db")
    dbstorage.save_jobs(jobs)

    # print(dbstorage.get_all_jobs())

    print(f"[SUCCESS] Completed scraping from {url}")



#Sample scraper(scraping a quotes website) to test the workflow.
# from src.utils import fetch_url
# from src.scrapers.quotes_scraper import parse
# from src.storage.csv_storage import CSVStorage
# from src.storage.db_storage import DBStorage

# def main():
#     url = "https://quotes.toscrape.com"
#     html = fetch_url(url)
#     if not html:
#         print("[ERROR] Could not fetch page.")
#         return
    
#     jobs = parse(html)
#     storage = CSVStorage("data/jobs.csv")
#     storage.save(jobs)

#     dbstorage = DBStorage("data/jobs.db")
#     dbstorage.save_jobs(jobs)

#     print("jobs")
#     print(dbstorage.get_all_jobs())

#     print(f"[SUCCESS] Completed scraping from {url}")

if __name__ == "__main__":
    main()
