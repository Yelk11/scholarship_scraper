from sys import orig_argv
from page_loader import Page_Loader
from scraper_db import Scraper_DB
from title_extractor import Title_Extractor
from requirement_extractor import Requirement_Extractor
from amount_extractor import Amount_Extractor
from org_extractor import Organization_Extractor
from deadline_extractor import Deadline_Extractor
from database import Database

class Scraper():
    
    def scrape(loader:Page_Loader):
        soup = loader.get_soup()
        title_extr = Title_Extractor(soup)
        req_extr = Requirement_Extractor(soup)
        amnt_extr = Amount_Extractor(soup)
        org_extr = Organization_Extractor(soup)
        deadline_extr = Deadline_Extractor(soup)

        db = Scraper_DB()
        db.insert(title=title_extr.extract, req=req_extr.extract(), amount=amnt_extr.extract(), org=org_extr.extract(), deadline=deadline_extr.extract())
        
    def scrape_main(self):
        database = Database()
        
        self.scrape()


