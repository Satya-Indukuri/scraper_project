# Job Listing Monitor

This project scrapes job listings from online job boards, stores them in CSV and SQLite databases, and can be extended for monitoring multiple job sites.

## Features

- Fetch jobs from RemoteOK using their API (faster and more reliable than HTML scraping)
- Deduplication to avoid storing duplicate jobs
- Storage in CSV and SQLite database
- Modular design for easy extension to other job sites
- Utility functions for fetching URLs and parsing HTML/JSON data

## Project Structure

```
job-monitor/
├── src/
│ ├── utils.py # Fetch URL helper
│ ├── scrapers/
│ │ ├── remoteok_scraper.py # RemoteOK API scraper
│ │ ├── quotes_scraper.py # Sample scraper using BeautifulSoup for testing the workflow
│ ├── storage/
│ │ ├── csv_storage.py # CSV storage
│ │ └── db_storage.py # SQLite storage
├── run_monitor.py # Main script to run the scraper
└── data/ # Stores jobs.csv and jobs.db
```

## Usage
Install dependencies:

pip install requests beautifulsoup4 lxml

Run the monitor(Go to job-monitor directory and run):

"python -m run_monitor"

Check stored jobs in data/jobs.csv or data/jobs.db.

Notes: 
RemoteOK jobs are fetched via their API because most jobs are dynamically loaded via JavaScript and cannot be reliably scraped with BeautifulSoup from raw HTML.
(quotes_scraper is a sample scraper i made using BeautifulSoup for testing the workflow.)

The project can be extended to scrape other job boards by creating new scraper modules following the same interface.