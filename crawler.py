from database import Database
from loader import Page_Loader
from validator import Validator
from collector import URL_Extractor

import time
import logging
from datetime import date

class Crawler():
    def __init__(self) -> None:
        logging.basicConfig(filename='crawler.log', encoding='utf-8', level=logging.DEBUG)
        self.db = Database()
    def crawl(self, url:str):
        page_loader = Page_Loader(url)
        
        if(page_loader.is_loaded()):
            url_extractor = URL_Extractor(soup=page_loader.get_soup(), url=url)
            
            scholarship_validator = Validator(soup=page_loader.get_soup())
            
            # get urls
            url_list = url_extractor.extract()
            # store urls
            if len(url_list) > 1:
                for url in url_list:
                    self.db.insert_url(url, False, str(date.today()))
            else:
                self.db.insert_url(url_list, False, str(date.today()))

            self.db.update_url(url, True, str(date.today()))

        
    def main_loop(self):
        while True:
            url = self.db.select_next_url()
            self.crawl(url)
            time.sleep(2)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.main_loop()