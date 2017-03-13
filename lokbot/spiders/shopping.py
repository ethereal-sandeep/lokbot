# -*- coding: utf-8 -*-

# author: zero

import scrapy


class ShoppingSpider(scrapy.Spider):
    name = "shopping"
    allowed_domains = ["shopping.com"]
    keyword = None
    page = None

    def __init__(self, keyword=None, page=None, *args, **kwargs):
        super(ShoppingSpider, self).__init__(*args, **kwargs)

        if keyword is None and page is None:
            # print usage message
            print "\n---------------------------------------------------------------------------------\n" \
                  "|                Error: No arguments supplied !!                                   |\n"\
                  "|                                                                                  |\n"\
                  "| usage: $ scrapy crawl shopping -a keyword=\"iphone\" -a page=2 -o output.json    |\n"\
                  "| usage: $ scrapy crawl shopping -a keyword=\"iphone 7 plus\" -o total_result.json |\n"\
                  " ----------------------------------------------------------------------------------\n"
            self.start_urls = []
            return

        self.keyword = keyword
        self.start_urls = ['http://shopping.com/products?KW=%s' % keyword]

        if page is not None:
            self.page = page
            self.start_urls = ['http://shopping.com/products~PG-' + page + '?KW=%s' % keyword]

    def parse(self, response):
        # do something here to make it cool :)
        pass

