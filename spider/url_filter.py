

from util.database import Database

class URL_Filter():
    def __init__(self) -> None:
        self.db = Database()

    def add(self, url:str, is_crawled:bool):
        if(self.db.check_duplicate(url)):
            self.db.add(url, is_crawled)


    
