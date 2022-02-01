from bs4 import BeautifulSoup
from util.page_loader import Page_Loader

import re
import json
# Helpful paper
# https://luca.ntop.org/LargeScaleWebClassification.pdf


class Scholarship_Validator():
    def __init__(self, soup:BeautifulSoup) -> None:
        self.my_soup = soup
        with open('schol_whitelist.json', 'r') as f:
            self.white_list = json.load(f)
        with open('schol_blacklist.json', 'r') as f:
            self.black_list = json.load(f)
        
    def validate(self) -> bool:
        return self.is_scholarship() or self.is_multi_scholarship()

    def is_scholarship(self) -> bool:
        for item in self.white_list["best"]:
            print('checking: ', item)
            print(len(self.my_soup.find_all(text=re.compile(item))))
        return len(self.my_soup.findAll(text=re.compile('scholarship'))) > 0
    
    def is_multi_scholarship(self) -> bool:
        for item in self.white_list["best"]:
            print('checking: ', item)
            print(len(self.my_soup.find_all(text=re.compile(item))))
        pass
        
        



if __name__ == '__main__':
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
    mult_schol_list = [
        # 'https://finaid.org/scholarships/',
        # 'https://studentscholarships.org',
        # 'https://signup.collegeboard.org/scholarship-search/',
        # 'https://bold.org/scholarships/easy-scholarships-list/',
        # 'https://www.fastweb.com',
        'https://www.fastweb.com/college-scholarships/articles/scholarships-for-average-students'
    ]
    none_list = [
        'https://studentaid.gov/understand-aid/types/scholarships',

    ]
    for url in schol_list:
        loader = Page_Loader(url)
        validator = Scholarship_Validator(loader.get_soup())
        print("Expected: True, result: ", validator.is_scholarship())
    
    for url in mult_schol_list:
        loader = Page_Loader(url)
        validator = Scholarship_Validator(loader.get_soup())
        print("Expected: True, result: ", validator.is_multi_scholarship())
    
    # for url in none_list:
    #     loader = Page_Loader(url)
    #     validator = Scholarship_Validator(loader.get_soup())
    #     print("Expected: False, result: ", validator.validate())
    