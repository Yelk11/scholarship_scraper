from crawler import Crawler

def main():
    print('starting scholarship scraper')
    # url = input('enter starting url: ')
    url = 'https://scholarshipamerica.org'
    crawler = Crawler()
    crawler.main_loop(url)

if __name__ == "__main__":
    main()


