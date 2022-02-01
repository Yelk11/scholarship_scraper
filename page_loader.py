import logging
from bs4 import BeautifulSoup
import requests
import random
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

class Page_Loader(str):

    def __init__(self, url):
        self.url = url
        self._is_loaded = False
        self.load_page(url)

    def load_page(self, url) -> bool:
        UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        )
        ua = UAS[random.randrange(len(UAS))]
        headers = {'user-agent': ua}
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)    
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        try:
            self.html_content = session.get(url, headers=headers).content
            self.soup = BeautifulSoup(self.html_content, "html.parser")
            self._is_loaded = True
        except Exception as e:
            logging.exception(e)
            # print(url)
            # print(e)
            self._is_loaded = False
        
            
    def is_loaded(self) -> bool:
        return self._is_loaded 
            
    def get_soup(self) -> BeautifulSoup:
        return self.soup

    def get_text(self) -> str:
        return self.html_content
    
    
    

        
        
        

        
