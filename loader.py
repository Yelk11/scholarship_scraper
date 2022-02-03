import logging
from bs4 import BeautifulSoup
from bs4.element import Comment
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
        # Different user-agent profiles
        UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        )
        ua = UAS[random.randrange(len(UAS))] # Pick random user-agent
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
            self._is_loaded = False
        
            
    def is_loaded(self) -> bool:
        return self._is_loaded 
            
    def get_soup(self) -> BeautifulSoup:
        if self._is_loaded:
            return self.soup
        else:
            return None
    
    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    
    def get_text(self) -> str:
        if self._is_loaded:
            texts = self.soup.findAll(text=True)
            visible_texts = filter(self.tag_visible, texts)  
            return u" ".join(t.strip() for t in visible_texts)
        else:
            return None
    
    
    



































if __name__ == "__main__":
    urls = [
        'https://www.nitrocollege.com/nitro-scholarship-application',
        'https://www.nitrocollege.com/scholarships',
        'https://usaccidentlawyer.com/the-law-offices-of-daniel-kim-scholarship/',
        'https://www.couponsplusdeals.com/scholarship',
        'https://www.dietspotlight.com/scholarship/essay/',
        'https://www.travelsafe-abroad.com/scholarship/',
        'https://www.loungelizard.com/scholarship/',
        'https://www.lasikplus.com/scholarship/',
        'https://firstsiteguide.com/scholarship/',
        'https://scholarships.mi.edu/esp-rock-guitar-scholarship/',
        'https://electricbikeslounge.com/scholarship/',
        'https://organicsbestshop.com/pages/superparent',
        'https://www.drivencoffee.com/scholarship/#scholarship-information',
        'https://accessscholarships.com/climate-justice-scholarship',
        'http://www.jumpstart-scholarship.net/application-us/',
        'https://www.homelight.com/scholarship/',
        'https://www.renthop.com/resources/college-scholarship',
        'https://www.vfw.org/assistance/student-veterans-support',
        'https://www.custodyxchange.com/scholarships/',
        'https://essentialtremor.org/resources/scholarships/',
        'https://www.iesabroad.org/scholarships-aid/hacu-ies-abroad-scholarship',
        'https://www.iesabroad.org/scholarships-aid/david-porter-scholarship',
        'https://www.hillandponton.com/veterans-scholarship/',
        'https://csdiw.org/scholarships/',
        'https://bigsunathletics.com',
        'https://www.mybiosource.com/scholarship-students-with-disabilities',
        'https://mus.edu/Prepare/Pay/Scholarships/2_Plus_2_Honor_Scholarship.html',
        'https://www.vdh.virginia.gov/health-equity/forms-and-applications/',
        'https://myalarmcenter.com/about/philanthropy/scholarships/',
        'https://www.tenshon.com/pages/scholarship',
        'https://www.hurstreview.com/AACN/',
        'https://www.lawyertime.com/gardiner-foundation-scholarship/',
        'https://www.sutliffstout.com/scholarship/',
        'https://www.winecountrygiftbaskets.com/information/scholarship.asp',
        'https://www.winecountrygiftbaskets.com/information/scholarship.asp',
        'https://apexminecrafthosting.com/minecraft-scholarship/',
        'https://www.cardrates.com/scholarship/',
        'https://www.royjorgensen.com/scholarships/',
        'https://www.aacnnursing.org/Students/Financial-Aid-Scholarships/Geraldine-Polly-Bednash-Scholarship',
        'https://www.renkinlaw.com/leukemia-lymphoma-law-school-scholarship/',
        'https://www.thezlawfirm.com/scholarship/',
        'https://www.cascadehealthcaresolutions.com/scholarships',
        'https://www.infinlaw.com/scholarship/',
        'https://www.confidentwriters.com/scholarship-essay-contest/',
        'http://www.cystinosisfoundation.org/Scholarship/',
        'https://solarpowernerd.com/scholarship/',
        'https://www.healthproductsforyou.com/scholarship.html',
        'https://www.healthproductsforyou.com/scholarship.html',
        'https://www.bestcollegereviews.org/inspired-greatness-scholarship/',
        'https://attorneyandrew.com/andrew-lynch-civil-justice-scholarship/',
        'https://www.capitalautoauction.com/about-us/scholarship',
        'https://www.lawnstarter.com/scholarship',
        'https://www.augmentedrealityrental.co/scholarship/',
        'https://myperfectplants.com/pages/scholarship-application#gbaid9533',
        'https://estavisa.com.au/scholarship/',
        'https://lindhfoster.com/eric-lindh-foster-law-llc-business-law-and-debtor-rights-scholarship/',
        'https://www.greatclubs.com/scholarship/',
        'https://www.achievetoday.com/scholarships',
        'https://www.capecodvacationrentals.com/annual-dream-vacation-scholarship/',
        'https://www.greenwellnesslife.com/scholarship/',
        'https://budgetbranders.com/scholarship/',
        'https://www.ownerdirect.com/scholarship',
        'https://www.in.gov/che/state-financial-aid/state-financial-aid-by-program/william-a-crawford-minority-teacher-scholarship/',
        'https://chasa.org/we-can-help/college-scholarships/',
        'https://florinroebig.com/scholarship/',
        'https://www.ambientbp.com/scholarship.php',
        'https://andrewmatherslaw.com/andrew-s-mathers-scholarship/',
        'https://www.abfse.org/html/post-graduate.html',
        'https://www.abfse.org/html/scholarships.html',
        'https://www.napabalawfoundation.org/scholarships',
        'https://www.vitalitymedical.com/scholarships-from-vitality-medical/disability-scholarship-program',
        'https://www.jonestshirts.com/pages/scholarship',
        'https://www.bestrateddocs.com/scholarships/',
        'https://catchingthedream.org',
        'https://criminallawyerwashingtondc.com/2022-make-a-difference-scholarship/',
        'https://mattresshelp.org/scholarship/',
        'https://mbainsight.com/mba-scholarships/',
        'http://www.digitalresponsibility.org/dont-text-and-drive-scholarship',
        'https://www.aacnnursing.org/Students/Graduate-Nursing-Student-Academy/CastleBranch-GNSA-Scholarship',
        'https://cedaredlending.com/scholarship/',
        'https://www.aftercollege.com/content/article/aftercollege-aacn-scholarship/?source=ur-discn',
        'https://www.beaweb.org/wp/scholarships/',
        'https://financialwolves.com/scholarship/',
        'https://www.shapeamerica.org/scholarships/billkanescholarship.aspx',
        'https://digitalroofingcompany.com/annual-digital-roofing-innovations-scholarship/',
        'https://www.vfw.org/community/youth-and-education/youth-scholarships',
        'https://www.unigo.com/scholarships/our-scholarships/zombie-apocalypse-scholarship',
        'https://www.myus.com/scholarships/the-community-scholarship/'
    ]
    num = 0
    for item in urls:
        num = num + 1
        loader = Page_Loader(item)
        with open('pages/' + str(num) + '.txt', 'w+') as file:
            file.write(loader.get_text())
