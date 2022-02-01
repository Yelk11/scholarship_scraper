import sqlite3


class URL_Frontier():
    def __init__(self) -> None:
        self.con = sqlite3.connect('scholarship.db')
    
    def get_next_url(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM url_tbl WHERE crawled='0'")
        url_list = cur.fetchall()
        return url_list[0][1]



if __name__ == "__main__":
    frontier = URL_Frontier()
    print(frontier.get_next_url())