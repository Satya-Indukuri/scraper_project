import os
import csv

class CSVStorage:
    def __init__(self, filename="data/jobs.csv"):
        self.filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def _load_existing(self):
        if not os.path.exists(self.filename):
            return set()

        existing = set()
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = f"{row['title']}::{row['company']}"
                existing.add(key)
        return existing

    def save(self, items):
        if not items:
            print("[WARN] No items to save.")
            return
        file_exists = os.path.isfile(self.filename)
        fieldnames = list(items[0].keys())

        existing_keys = self._load_existing()
        new_items = []
        for item in items:
            key = f"{item['title']}::{item['company']}"
            if key not in existing_keys:
                new_items.append(item)
                existing_keys.add(key)

        if not new_items:
            print("[INFO] No new data to add.")
            return

        with open(self.filename,"a", newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(new_items)

        print(f"[INFO] Saved {len(new_items)} rows to {self.filename}")

# #run as a module from the "job-monitor" directoty to test this script with below code
# data = [
#     {"title": "Test1", "company": "Author1", "location": "tag1", "url": "https://a", "posted_date": None, "source": "test"},
#     {"title": "Test2", "company": "Author2", "location": "tag2", "url": "https://b", "posted_date": None, "source": "test"}
# ]

# storage = CSVStorage("src/data/jobs.csv")
# storage.save(data)