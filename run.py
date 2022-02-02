from spider import Crawler

def main():
    print('starting scholarship scraper')
    url = input('enter starting url: ')
    crawler = Crawler()
    crawler.main_loop()

if __name__ == "__main__":
    main()


