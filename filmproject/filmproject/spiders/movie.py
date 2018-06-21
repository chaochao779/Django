# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['http://www.ygdy8.com']
    start_urls = ['http://http://www.ygdy8.com/']

    def parse(self, response):
        pass
