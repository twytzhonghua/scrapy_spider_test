# -*- coding: utf-8 -*-
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.statscollectors import *
from scrapy.extensions import *
from scrapy.extensions.telnet import *
from scrapy.extensions.throttle import *
from scrapy.extensions.corestats import *
from scrapy.extensions.closespider import *
from scrapy.extensions.memdebug import *
from scrapy.extensions.memusage import *
from scrapy.extensions.feedexport import *
from scrapy.extensions.spiderstate import *
from scrapy.extensions.logstats import *
from scrapy.core.scheduler import *
from scrapy.core.downloader import *
from scrapy.downloadermiddlewares import *
from scrapy.downloadermiddlewares.robotstxt import *
from scrapy.downloadermiddlewares.httpauth import *
from scrapy.downloadermiddlewares.downloadtimeout import *
from scrapy.downloadermiddlewares.defaultheaders import *
from scrapy.downloadermiddlewares.useragent import *
from scrapy.downloadermiddlewares.retry import *
from scrapy.downloadermiddlewares.ajaxcrawl import *
from scrapy.downloadermiddlewares.redirect import *
from scrapy.downloadermiddlewares.httpcompression import *
from scrapy.downloadermiddlewares.cookies import *
from scrapy.downloadermiddlewares.httpproxy import *
from scrapy.downloadermiddlewares.chunked import *
from scrapy.downloadermiddlewares.stats import *
from scrapy.downloadermiddlewares.httpcache import *
from scrapy.spidermiddlewares import *
from scrapy.spidermiddlewares.httperror import *
from scrapy.spidermiddlewares.offsite import *
from scrapy.spidermiddlewares.referer import *
from scrapy.spidermiddlewares.urllength import *
from scrapy.spidermiddlewares.depth import *
from scrapy.pipelines import *
from scrapy.dupefilters import *
from queuelib import *
from scrapy.squeues import *
from scrapy.core.downloader.handlers.http import *
from scrapy.core.downloader.contextfactory import *

from scrapy.logformatter import *
from scrapy import *


from stockCowTools.spiders.ThsGuDong2 import ThsgudongSpider
from stockCowTools.spiders.stockSql import *
from stockCowTools.spiders.dataHtmlParse import *
from stockCowTools.spiders.DzhGuDong import DzhgudongSpider
from stockCowTools.spiders.update_stock import * 

def LtGDSpiderStart():
    process = CrawlerProcess()
    process.crawl(DzhgudongSpider)
    process.start()

if __name__ == "__main__":
    LtGDSpiderStart()
    

    
    

    
