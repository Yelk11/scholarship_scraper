from loader import Page_Loader
from collector import Title_Extractor
from collector import Requirement_Extractor
from collector import Amount_Extractor
from collector import Organization_Extractor
from collector import Deadline_Extractor
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
        self.scrape()


