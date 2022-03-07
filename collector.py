from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from pyparsing import col
import spacy

'''
https://spacy.io
https://spacy.io/api/entityrecognizer

use entity recognition


'''


# TODO: implement Title extractor
class Collector():
    def __init__(self, string:str, soup:BeautifulSoup) -> None:
        self.input_str = string
        self.soup = soup
        self.nlp = spacy.load("en_core_web_sm") 
        self.doc = self.nlp(self.input_str)
        
    
    def get_title(self) -> str:
        for token in self.doc[:10]:
            print(token)
            print(token.ent_type_)
        return self.input_str
    
    def get_deadline(self) -> str:
        pass
    
    def get_organization(self) -> str:
        pass
    
    def get_amount(self) -> int:
        self.amount = 0
        amount_list = self.soup.find_all(['strong','p', 'h1', 'h2', 'h3', 'span', 'b'])
        results = re.search('\$\d+(,|\d)\d+', str(amount_list))
        if results:
            return results.group(0)
        return self.amount
    
    def get_requirements(self):
        pass


        

# TODO handle /index.html type urls by adding appening to base url
class URL_Extractor():
    def __init__(self, soup:BeautifulSoup, url:str) -> None:
        self.URL_list = []
        self.my_soup = soup
        self.url = url
    
    def extract(self) -> list[str]:
        new_list = []
        for link in self.my_soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(self.url, path)
            print(path)
            new_list.append(path)
        return new_list
        # new_list = []
        # for item in self.my_soup.find_all('a', 
        #                   attrs={'href': re.compile("^https://")}):
        #     new_list.append(self.url_builder(item['href']))
        #     print(self.url_builder(item['href']))
        # return new_list
    
        

if __name__ == '__main__':
    from loader import Page_Loader
    schol_list = [
        # 'https://www.nitrocollege.com/nitro-scholarship-application?utm_source=cpc&utm_medium=studentscholarships&utm_campaign=studentscholarships.org_student_2K',
        # 'https://www.niche.com/colleges/scholarships/no-essay-scholarship/?utm_source=Fastweb&utm_medium=Referral&utm_campaign=FWnes',
        # 'https://www.fastweb.com/college-scholarships/scholarships/154428-albert-b-allison-memorial-endowed-scholarship',
        # 'https://www.fastweb.com/college-scholarships/scholarships/103541-church-vocation-grant-emory-henry-college',
        # 'https://www.fastweb.com/college-scholarships/scholarships/103543-music-and-theater-scholarship-emory-and-henry-college',
        # 'https://www.fastweb.com/college-scholarships/scholarships/103544-pre-med-scholarship-emory-henry-college',
        # 'https://www.fastweb.com/college-scholarships/scholarships/108168-james-and-nancy-johnson-scholarship-in-the-college-of-engineering',
        # 'https://www.fastweb.com/college-scholarships/scholarships/108169-union-contractors-of-agc-minority-scholarship',
        # 'https://www.fastweb.com/college-scholarships/scholarships/108173-rob-johnson-memorial-scholarship',
        # 'https://www.fastweb.com/college-scholarships/scholarships/108190-jennings-coe-family-scholarship',
        # 'https://www.fastweb.com/college-scholarships/scholarships/113860-adam-andrews-memorial-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/113861-athletic-scholarship-howard-college'

    ]

    for url in schol_list:
        loader = Page_Loader(url)
        collector = Collector(loader.get_text(),loader.get_soup())
        collector.get_title()
        
