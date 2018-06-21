# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class FilmSpider(RedisCrawlSpider):
    name = 'film'
    allowed_domains = ['www.ygdy8.com']
    start_urls = ['https://www.dy2018.com/0/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # name = response.xpath('//a[@class="ulink"]/text()').extrat

        tables = response.xpath('//table[@class="tbspan"]')
        for i in tables:
            name = i.xpath('//')
        return i

