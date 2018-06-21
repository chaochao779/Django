# -*- coding: utf-8 -*-
import scrapy
import urllib
import urllib.request
from PIL import Image

from scrapy_redis.spiders import Spider ,CrawlSpider

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    # get请求
    start_urls = ['https://www.douban.com/accounts/login']

    # 模拟豆瓣登录：第一步发起get请求，登录界面，获取验证码
    # 第二步post请求，根据第一步获取的数据
    def parse(self, response):
        captcha_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        # 没有验证码
        if not captcha_url:
            # 更简单
            form = {'email':'18513106743',
                    'password':'31415926abc'}
            pass
        else:#验证
            urllib.request.urlretrieve(captcha_url, './captcha.png')
            Image.open('./captcha.png').show()

            code = input('请输入验证码：')
            username = '18513106743'
            pwd = '31415926abc'

            form = {'email': username,
                    'password': pwd,
                    'captcha': code}

        # 发起post
        post_url = 'https://www.douban.com/login/'
        yield scrapy.FormRequest(url=post_url,formdata=form,callback=self.parse_post)

    def parse_post(self,response):
#         将数据保存一下
        text = response.text
        # 登录成功了
        # 继续发起请求
        person_url = 'https://www.douban.com/people/164698173/'
        # 默认情况下cookie保存的，登录成功了，进行get请求获取用户界面
        #  get 请求
        yield scrapy.Request(url=person_url,callback=self.parse_person)

    def parse_person(self,response):
        # 使用xpath提取想要的数据
        pass