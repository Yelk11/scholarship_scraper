from bs4 import BeautifulSoup
import re
import json
import os
import numpy as np


# Helpful paper
# https://luca.ntop.org/LargeScaleWebClassification.pdf
'''
create a distrobution of sholarship data
then look to see if there is a cutoff point between lists of scholarships and a single one
as well as non-scholarship like pages
'''



class Validator():
    def __init__(self, text:str) -> None:
        self.text = text
        with open('keywords.json', 'r') as f:
            self.keywords = json.load(f)
    
    def validate(self) -> bool:
        x0 = self.extract_keywords(self.text)
        perc = self.percentage(len(x0), len(self.keywords['keywords']))
        return perc

    def percentage(self, x1, x2):
        try:
            print(f"{x1} : {x2}")
            ans = float(x1)/float(x2)
            ans=ans*100
        except:
            return 0 # for div by 0 errors
        else:
            return ans
    
    def extract_keywords(self, text:str):
        new_list = []
        for item in text.split():
            if item in self.keywords['keywords'] and item not in new_list:
                new_list.append(item)
        return new_list


if __name__ == '__main__':
    from loader import Page_Loader
    schol_list = [
        'https://www.nitrocollege.com/nitro-scholarship-application?utm_source=cpc&utm_medium=studentscholarships&utm_campaign=studentscholarships.org_student_2K',
        'https://www.niche.com/colleges/scholarships/no-essay-scholarship/?utm_source=Fastweb&utm_medium=Referral&utm_campaign=FWnes',
        'https://www.fastweb.com/college-scholarships/scholarships/154428-albert-b-allison-memorial-endowed-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/103541-church-vocation-grant-emory-henry-college',
        'https://www.fastweb.com/college-scholarships/scholarships/103543-music-and-theater-scholarship-emory-and-henry-college',
        'https://www.fastweb.com/college-scholarships/scholarships/103544-pre-med-scholarship-emory-henry-college',
        'https://www.fastweb.com/college-scholarships/scholarships/108168-james-and-nancy-johnson-scholarship-in-the-college-of-engineering',
        'https://www.fastweb.com/college-scholarships/scholarships/108169-union-contractors-of-agc-minority-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/108173-rob-johnson-memorial-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/108190-jennings-coe-family-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/113860-adam-andrews-memorial-scholarship',
        'https://www.fastweb.com/college-scholarships/scholarships/113861-athletic-scholarship-howard-college'

    ]
    mult_schol_list = [
        # 'https://finaid.org/scholarships/',
        # 'https://studentscholarships.org',
        # 'https://signup.collegeboard.org/scholarship-search/',
        # 'https://bold.org/scholarships/easy-scholarships-list/',
        'https://www.fastweb.com',
        'https://www.fastweb.com/college-scholarships/articles/scholarships-for-average-students'
    ]
    none_list = [
        # 'https://studentaid.gov/understand-aid/types/scholarships',

    ]
    # one scholarship
    for url in schol_list:
        loader = Page_Loader(url)
        validator = Validator(loader.get_text())
        print("Expected: True, result: ", validator.validate())
    
    #  list of scholarships
    for url in mult_schol_list:
        loader = Page_Loader(url)
        validator = Validator(loader.get_text())
        print("Expected: True, result: ", validator.validate())
    
    # no scholarship
    for url in none_list:
        loader = Page_Loader(url)
        validator = Validator(loader.get_text())
        print("Expected: False, result: ", validator.validate())
    