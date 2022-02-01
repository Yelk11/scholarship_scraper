import logging
import sqlite3
from datetime import date


class Database():
    def __init__(self) -> None:
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute('''CREATE TABLE IF NOT EXISTS url_tbl (
	        url_id INTEGER PRIMARY KEY,
	        url TEXT NOT NULL,
	        crawled INTEGER NOT NULL,
	        date_accessed TEXT NOT NULL
        );''')
        con.commit()
        con.close()

    def add(self, url: str, is_crawled: bool):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("INSERT INTO url_tbl(url, crawled, date_accessed) VALUES (?,?,?)",
                       (url, is_crawled, str(date.today())))
        con.commit()
        con.close()

    def check_duplicate(self, url:str) -> bool:
        try:
            con = sqlite3.connect('scholarship.db')
            curser = con.cursor()
            curser.execute(
                """SELECT EXISTS(SELECT 1 FROM url_tbl WHERE url=?);""", (url,))
            my_var = curser.fetchall()
            con.commit()
            con.close()
            return my_var
        except Exception as e:
            logging.error('Url: %s',url)
            logging.error(e)
            # print('Url: %s',url)
            # print(e)


    def print_all(self):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""SELECT * FROM url_tbl;""")
        con.commit()
        for item in curser.fetchall():
            print(item)
        con.close()

    def del_item(self, url):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""DELETE FROM url_tbl WHERE url=?;""", (url,))
        con.commit()
        con.close()

    def delete_all(self):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""DELETE FROM url_tbl;""")
        con.commit()
        con.close()

    def set_crawled(self, url):
        con = sqlite3.connect('scholarship.db')
        curser = con.cursor()
        curser.execute("""UPDATE url_tbl SET crawled=1 WHERE url=?;""", (url,))
        con.commit()
        con.close()

if __name__ == "__main__":
    database = Database()
    url_list = [
        'https://www.nitrocollege.com/nitro-scholarship-application',
        'https://www.nitrocollege.com/nitro-scholarship-application',
        'https://calvinrosser.com/scholarships/buena-amistad-scholarship/',
        'https://joinjuno.com/scholarship/january-2022-scholarship',
        'https://www.keepgoingforward.org/money-isnt-everything',
        'https://calvinrosser.com/scholarships/financial-freedom/',
        'https://calvinrosser.com/scholarships/a-bold-life-scholarship/',
        'https://www.nitrocollege.com/nitro-scholarship-application/1k',
        'https://calvinrosser.com/scholarships/a-green-world-scholarship/',
        'https://www.mymozaic.com/monthlyscholarship.php'
    ]
    for item in url_list:
        database.add(item, False)
