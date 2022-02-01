from database import Database
from url_frontier import URL_Frontier
from page_loader import Page_Loader
from scholarship_validator import Scholarship_Validator
from url_extractor import URL_Extractor
from url_filter import URL_Filter

import time
import logging


class Crawler():
    def __init__(self) -> None:
        logging.basicConfig(filename='crawler.log', encoding='utf-8', level=logging.DEBUG)

    def crawl(self, url:str):
        page_loader = Page_Loader(url)
        db = Database()
        if(page_loader.is_loaded()):
            url_extractor = URL_Extractor(soup=page_loader.get_soup(), url=url)
            
            scholarship_validator = Scholarship_Validator(soup=page_loader.get_soup())
            url_filter = URL_Filter()
            # get urls
            url_list = url_extractor.extract()
            # store urls
            if len(url_list) > 1:
                for url in url_list:
                    url_filter.add(url, False)
                else:
                    url_filter.add(url_list, False)

            db.set_crawled(url)

        
    def main_loop(self):
        url_frontier = URL_Frontier()
        while True:
            url = url_frontier.get_next_url()
            self.crawl(url)
            time.sleep(2)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.main_loop()