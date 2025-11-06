"""
RemoteOK Scraper using API

Explanation:
- Instead of scraping the HTML with BeautifulSoup, we use the RemoteOK JSON API endpoint (/api).
- Reason: Most job listings on RemoteOK are loaded dynamically via JavaScript, so scraping the raw HTML would miss many jobs.
- The API provides structured JSON data directly, which is faster, more reliable, and easier to parse.
- This approach avoids issues with page layout changes and ensures we get all available job listings efficiently.
"""

from src.utils import fetch_url
import requests

def parse_remoteok_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0 (JobMonitorBot/1.0; +https://example.com)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # First element is metadata, skip it
        jobs_raw = data[1:]  
        jobs_data = []

        for job in jobs_raw:
            j = {
                "title": job.get("position"),
                "company": job.get("company"),
                "location": job.get("location", "Remote"),
                "url": job.get("url"),
                "posted_date": job.get("date"),
                "salary": job.get("salary", ""),
                "source": "RemoteOK"
            }
            jobs_data.append(j)

        print(f"[INFO] Parsed {len(jobs_data)} jobs from RemoteOK")
        return jobs_data

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] RemoteOK fetch failed: {e}")
        return []


# from bs4 import BeautifulSoup
# from src.utils import fetch_url
# from datetime import datetime
# import re

# def parse(html, base_url="https://remoteok.com/"):
#     soup = BeautifulSoup(html, "lxml")
#     print(soup.prettify()[0:1000])
#     print("title")
#     print(soup.find("title"))

#     jobs_data = []
#     jobs = soup.find_all("tr",id_="job-1128869")
#     print(len(jobs))
#     for job in jobs:
#         print(job)
#         title = job.find("h2",itemprop_="title")
#         company = job.find("h3",itemprop_="name")
#         link = job.find("a",class_="preventLink")
#         locations = [location.get_text(strip=True) for location in job.find_all("div",class_=re.compile(r'^location$'))]
#         time = job.find("time")
#         salary = job.find("div",class_="salary")

#         if not title or not company or not link:
#             print(title, company, link)
#             continue

#         j = {
#             "title":title.get_text(strip=True),
#             "company":company.get_text(strip=True),
#             "location":",".join(locations),
#             "url":base_url+link.get("href"),
#             "posted_date":time.get("datetime"),
#             "salary":salary.get_text(strip=True),
#             "source":"https://remoteok.com/"
#         }

#         jobs_data.append(j)

#     print(f"[INFO] Parsed {len(jobs_data)} jobs from RemoteOK")
#     return jobs_data

    

        