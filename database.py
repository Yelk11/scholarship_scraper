import logging
import sqlite3
from datetime import date
import os

class Database():
    def __init__(self) -> None:
        print()
        self.db_path = os.getcwd() + '/data/scholarship.db'
        self.create_url_tbl()
        self.create_scholarship_tbl()
    
    def create_url_tbl(self):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute('''CREATE TABLE IF NOT EXISTS url_tbl (
	        url_id INTEGER PRIMARY KEY,
	        url TEXT UNIQUE NOT NULL,
	        iscrawled INTEGER NOT NULL,
	        date_accessed TEXT NOT NULL
        );''')
        con.commit()
        con.close()

    def create_scholarship_tbl(self):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute('''CREATE TABLE IF NOT EXISTS scholarship_tbl (
	        schol_id INTEGER PRIMARY KEY,
	        url TEXT UNIQUE NOT NULL,
	        date_accessed TEXT NOT NULL,
            title TEXT NOT NULL,
            requirements TEXT NOT NULL,
            amount INTEGER NOT NULL,
            organization TEXT NOT NULL,
            deadline TEXT NOT NULL
        );''')
        con.commit()
        con.close()
    
    def insert_url(self, url: str, is_crawled: bool, date_accessed):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        try:
            curser.execute(f"""
            INSERT INTO 
                url_tbl(url, iscrawled, date_accessed) 
            VALUES 
                (?,?,?)""", (url,is_crawled,date_accessed))
        except sqlite3.IntegrityError:
            pass
        except Exception as e:
            print(f"Exception: {e} on url: {url}")
        con.commit()
        con.close()
    
    def insert_scholarship(self, url:str, title:str, reqs:str, amount:int, org:str, deadline:str):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        try:
            curser.execute(f"""
            INSERT OR IGNORE INTO 
                scholarship_tbl(url, date_accessed, title, requirements, amount, organization, deadline) 
            VALUES
                (?,?,?,?,?,?,?)""",
                        (url, str(date.today()), title, reqs, amount, org, deadline))
        except Exception as e:
            print(f"Exception: {e} on url: {url}")
        con.commit()
        con.close()

    def delete_url(self, url):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute("""DELETE FROM url_tbl WHERE url=?;""", (url,))
        con.commit()
        con.close()

    def delete_all_urls(self):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute("""DELETE FROM url_tbl;""")
        con.commit()
        con.close()

    def update_url(self,url, iscrawled, date_accessed):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute(f"""
        UPDATE 
            url_tbl 
        SET 
            iscrawled = ?,
            date_accessed = ?
        WHERE 
            url=?;
            """, (iscrawled, date_accessed, url))
        con.commit()
        con.close()
    
    def update_scholarship(self, url, date_accessed, title, requirements, amount, organization, deadline):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute(f"""
        UPDATE 
            scholarship_tbl 
        SET 
	        date_accessed = {date_accessed},
            title = {title},
            requirements = {requirements},
            amount = {amount},
            organization = {organization},
            deadline = {deadline}
        WHERE 
            url={url};
        """)
        con.commit()
        con.close()

    def select_next_url(self):
        con = sqlite3.connect(self.db_path)
        curser = con.cursor()
        curser.execute(f"""
        SELECT 1 FROM  
            url_tbl 
        WHERE 
            iscrawled={False};
        """)
        con.commit()
        con.close()


if __name__ == "__main__":
    db = Database()
    # url_list = [
    #     'https://www.nitrocollege.com/nitro-scholarship-application',
    #     'https://www.nitrocollege.com/nitro-scholarship-application',
    #     'https://calvinrosser.com/scholarships/buena-amistad-scholarship/',
    #     'https://joinjuno.com/scholarship/january-2022-scholarship',
    #     'https://www.keepgoingforward.org/money-isnt-everything',
    #     'https://calvinrosser.com/scholarships/financial-freedom/',
    #     'https://calvinrosser.com/scholarships/a-bold-life-scholarship/',
    #     'https://www.nitrocollege.com/nitro-scholarship-application/1k',
    #     'https://calvinrosser.com/scholarships/a-green-world-scholarship/',
    #     'https://www.mymozaic.com/monthlyscholarship.php'
    # ]
    # for item in url_list:
    #     db.insert_url(item, False, str(date.today()))
    db.delete_all_urls()

