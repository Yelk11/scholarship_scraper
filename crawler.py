from database import Database
from loader import Page_Loader
from validator import Validator
from scraper import Scraper

import time
import logging
from datetime import date
from urllib.parse import urljoin

class Crawler():
    def __init__(self) -> None:
        logging.basicConfig(filename='crawler.log', encoding='utf-8', level=logging.DEBUG)
        self.db = Database()
        self.scraper = Scraper()
    
    def crawl(self, url:str):
        print(f'crawling {url}')
        page_loader = Page_Loader(url)
        
        if(page_loader.is_loaded()):
            
            validator = Validator(page_loader.get_text())
            #  if it is a scholarship, scrape it
            if validator.validate():
                print(f'{url} is a scholarship')
                self.scraper.scrape(page_loader)
            # get urls
            url_list = self.extract_url(page_loader.get_soup(), url)
            # store urls
            if len(url_list) > 1:
                for item in url_list:
                    self.db.insert_url(item, False, str(date.today()))
            else:
                self.db.insert_url(url_list, False, str(date.today()))
            
            self.db.update_url(url, True, str(date.today()))

    def extract_url(self, soup, url) -> list[str]:
        new_list = []
        for link in self.soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(self.url, path)
            print(path)
            new_list.append(path)
        return new_list
    
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


if __name__ == "__main__":
    c = Crawler()
    c.crawl('https://joinjuno.com/scholarship/january-2022-scholarship')
