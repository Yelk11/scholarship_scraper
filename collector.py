from bs4 import BeautifulSoup
import re

class Title_Extractor():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.my_soup = soup
    
    def extract(self):
        pass

    def get_title(self):
        pass

class Deadline_Extractor():
    def __init__(self) -> None:
        self.deadline = ''
    def extract(self):
        pass
class Organization_Extractor:
    def __init__(self, soup:BeautifulSoup) -> None:
        self.soup = soup

    def extract():
        pass

class Amount_Extractor():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.soup = soup
        self.amount = 0
    
    def extract(self) -> int:
        amount_list = self.soup.find_all(['strong','p', 'h1', 'h2', 'h3', 'span', 'b'])
        results = re.search('\$\d+(,|\d)\d+', str(amount_list))
        if results:
            return results.group(0)
        return self.amount

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

class Requirement_Extractor():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.requirements = []
    
    def extract(self):
        pass
