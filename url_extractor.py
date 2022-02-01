from bs4 import BeautifulSoup

class URL_Extractor():
    def __init__(self, soup:BeautifulSoup, url:str) -> None:
        self.URL_list = []
        self.my_soup = soup
        self.url = url
    
    def extract(self) -> list[str]:
        new_list = []
        for item in self.my_soup.find_all('a', href=True):
            new_list.append(item['href'])
        return new_list