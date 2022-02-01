import logging
import sqlite3
from datetime import date


class Scraper_DB():
    def __init__(self) -> None:
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute('''CREATE TABLE IF NOT EXISTS scholarship_tbl (
	        schol_id INTEGER PRIMARY KEY,
	        url TEXT NOT NULL,
	        date_accessed TEXT NOT NULL,
            title TEXT NOT NULL,
            requirements TEXT NOT NULL,
            amount INTEGER NOT NULL,
            organization TEXT NOT NULL,
            deadline TEXT NOT NULL
        );''')
        con.commit()
        con.close()

    def insert(self, url:str, title:str, req:str, amount:int, org:str, deadline:str):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("INSERT INTO scholarship_tbl(url, date_accessed, title, requirements, amount, organization, deadline) VALUES (?,?,?,?,?,?,?)",
                       (url, str(date.today()), title, req, amount, org, deadline))
        con.commit()
        con.close()

    def print_all(self):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""SELECT * FROM scholarship_tbl;""")
        con.commit()
        for item in curser.fetchall():
            print(item)
        con.close()

    def del_item(self, url):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""DELETE FROM scholarship_tbl WHERE url=?;""", (url,))
        con.commit()
        con.close()

    def delete_all(self):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""DELETE FROM scholarship_tbl;""")
        con.commit()
        con.close()

if __name__ == "__main__":
    database = Scraper_DB()
    
    
