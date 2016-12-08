from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals

from testbaidu.spiders.tbaidu import TbaiduSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TbaiduSpider)
process.start() # the script will block here until the crawling is finished