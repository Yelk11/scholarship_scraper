from bs4 import BeautifulSoup
import re

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


