from bs4 import BeautifulSoup


class Requirement_Extractor():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.requirements = []
    
    def extract(self):
        pass