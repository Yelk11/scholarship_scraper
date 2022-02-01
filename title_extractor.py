from bs4 import BeautifulSoup


class Title_Extractor():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.my_soup = soup
    
    def extract(self):
        pass

    def get_title(self):
        