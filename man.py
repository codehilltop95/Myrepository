import urllib.request as s
from bs4 import BeautifulSoup
class scraper:
    def __init__(self,name):
        self.site=name
    def scrape(self,m):
        r=s.urlopen(self.site)
        print(r)
        self.variable=m
site=scraper("https://news.google.com")
site.scrape(1)
print(site.variable)