# -*- coding: utf-8 -*-

# author: zero

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LokbotItem(scrapy.Item):
    # product model here
    pass


class LokbotTotalItem(scrapy.Item):
    # total result count model here
    pass


class Status(scrapy.Item):
    # common status message here
    pass