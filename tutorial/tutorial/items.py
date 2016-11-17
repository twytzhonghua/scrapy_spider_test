# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name = scrapy.Field()
	stock_number = scrapy.Field()
	hold_number  = scrapy.Field()
	percent = scrapy.Field()
	types = scrapy.Field()
	time = scrapy.Field()
	nr = scrapy.Field()
	stockType = scrapy.Field()
	memType = scrapy.Field()

