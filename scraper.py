from loader import Page_Loader
from collector import Collector
from database import Database

class Scraper():
    
    def scrape(loader:Page_Loader):
        soup = loader.get_soup()
        collector = Collector(soup)

        db = Database()
        db.insert_scholarship(title=collector.get_title(), req=collector.get_requirements(), amount=collector.get_amount(), org=collector.get_org(), deadline=collector.get_deadline())
        


