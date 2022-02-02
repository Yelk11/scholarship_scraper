from sys import orig_argv
from loader import Page_Loader
from title import Title_Extractor
from requirement import Requirement_Extractor
from amount import Amount_Extractor
from organization import Organization_Extractor
from deadline import Deadline_Extractor
from database import Database

class Scraper():
    
    def scrape(loader:Page_Loader):
        soup = loader.get_soup()
        title_extr = Title_Extractor(soup)
        req_extr = Requirement_Extractor(soup)
        amnt_extr = Amount_Extractor(soup)
        org_extr = Organization_Extractor(soup)
        deadline_extr = Deadline_Extractor(soup)

        db = Database()
        db.insert_scholarship(title=title_extr.extract, req=req_extr.extract(), amount=amnt_extr.extract(), org=org_extr.extract(), deadline=deadline_extr.extract())
        
    def scrape_main(self):
        database = Database()
        
        self.scrape()


