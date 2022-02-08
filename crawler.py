from database import Database
from loader import Page_Loader
from validator import Validator
from collector import URL_Extractor
from scraper import Scraper

import time
import logging
from datetime import date

class Crawler():
    def __init__(self) -> None:
        logging.basicConfig(filename='crawler.log', encoding='utf-8', level=logging.DEBUG)
        self.db = Database()
        self.scraper = Scraper()
    
    def crawl(self, url:str):
        print(f'crawling {url}')
        page_loader = Page_Loader(url)
        
        if(page_loader.is_loaded()):
            url_extractor = URL_Extractor(page_loader.get_soup(), url=url)
            validator = Validator(page_loader.get_text())
            #  if it is a scholarship, scrape it
            if validator.validate():
                print(f'{url} is a scholarship')
                self.scraper.scrape(page_loader)
            # get urls
            url_list = url_extractor.extract()
            # store urls
            if len(url_list) > 1:
                for url in url_list:
                    self.db.insert_url(url, False, str(date.today()))
            else:
                self.db.insert_url(url_list, False, str(date.today()))
            # TODO iscrawled flag is not being updated in database
            self.db.update_url(url, 1, str(date.today()))

        
    def main_loop(self, starting_url):
        self.crawl(starting_url)
        while True:
            url = self.db.select_next_url()
            if url != None:
                self.crawl(url)
                time.sleep(2)
            else:
                print('no more urls found')
                break


