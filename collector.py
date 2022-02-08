from bs4 import BeautifulSoup
import re

from loader import Page_Loader




class Collector():
    def __init__(self, soup:BeautifulSoup):
        self.soup = soup
# TODO: implement Title extractor
    def get_title(self):
        pass
# TODO implement Deadline Extractor
    def get_deadline(self):
        pass
# TODO implement org extractor
    def get_org(self):
        pass
    def get_amount(self) -> int:
        amount_list = self.soup.find_all(['strong','p', 'h1', 'h2', 'h3', 'span', 'b'])
        results = re.search('\$\d+(,|\d)\d+', str(amount_list))
        if results:
            return results.group(0)
        else:
            return -1
    def get_requirements(self):
        pass

if __name__ == '__main__':
    loader = Page_Loader('https://calvinrosser.com/scholarships/a-green-world-scholarship/')
    col = Collector(loader.get_soup())
    print(col.get_title())
    print(col.get_amount())
    print(col.get_deadline())
    print(col.get_org())
    print(col.get_requirements())

