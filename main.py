from crawler import Crawler

def main():
    print('starting scholarship scraper')
    # url = input('enter starting url: ')
    url = 'https://studentaid.gov/understand-aid/types/scholarships'
    crawler = Crawler()
    crawler.main_loop(url)

if __name__ == "__main__":
    main()


