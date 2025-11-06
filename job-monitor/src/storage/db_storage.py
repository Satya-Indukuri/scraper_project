import sqlite3
import os

class DBStorage:
    def __init__(self, db_path="data/jobs.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    company TEXT,
                    location TEXT,
                    url TEXT,
                    posted_date TEXT,
                    salary TEXT,
                    source TEXT,
                    UNIQUE(title, company)
                );
            """)
            conn.commit()

    def save_jobs(self, jobs):
        if not jobs:
            print("[WARN] No jobs to save.")
            return

        with self._connect() as conn:
            cursor = conn.cursor()
            added_count = 0
            for job in jobs:
                try:
                    cursor.execute("""
                    INSERT INTO jobs (title, company, location, url, posted_date, salary, source) 
                    VALUES (?,?,?,?,?,?,?) """,(
                        job.get('title'),
                        job.get("company"),
                        job.get("location"),
                        job.get("url"),
                        job.get("posted_date"),
                        job.get("salary"),
                        job.get("source")
                    ))
                    added_count += 1
                except sqlite3.IntegrityError:
                    # if the job is a repeated(duplicate) based on (title, company), cause it is given as UNIQUE when creating the table
                    continue
            conn.commit()
        print(f"[INFO] Added {added_count} new jobs to DB.")

    def get_all_jobs(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * from jobs")
            rows = cursor.fetchall()
        return rows
                    












        