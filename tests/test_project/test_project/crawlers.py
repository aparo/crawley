from crawley.crawlers import BaseCrawler
from crawley.scrapers.smart import SmartScraper
from crawley.extractors import XPathExtractor
from models import *

class PackagesAuthorsScraper(SmartScraper):

    #The pages that have the precious data
    matching_urls = ["%pypi.python.org/pypi/%"]
    
    #an example of a page that you want to scrap
    template_url = "http://pypi.python.org/pypi/Shake/0.5.10"

    def scrape(self, response):

        project = response.html.xpath("/html/body/div[5]/div/div/div[3]/h1")[0].text
        author = response.html.xpath("/html/body/div[5]/div/div/div[3]/ul/li/span")[0].text

        PackagesAuthors(project=project, author=author)


class PackagesAuthorsCrawler(BaseCrawler):

    #add your starting urls here
    start_urls = ["http://pypi.python.org/pypi"]

    #add your scraper classes here
    scrapers = [PackagesAuthorsScraper]

    #specify you maximum crawling depth level
    max_depth = 1

    #select your favourite HTML parsing tool
    extractor = XPathExtractor
