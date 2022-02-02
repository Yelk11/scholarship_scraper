from sys import orig_argv
from util.page_loader import Page_Loader
from util.a_other_db import Scraper_DB
from scraper.title_extractor import Title_Extractor
from scraper.requirement_extractor import Requirement_Extractor
from scraper.amount_extractor import Amount_Extractor
from scraper.org_extractor import Organization_Extractor
from scraper.deadline_extractor import Deadline_Extractor
from util.database import Database

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


