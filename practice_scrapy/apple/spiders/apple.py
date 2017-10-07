# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem

class AppleSpider(scrapy.Spider):
    name = "apple"
    start_urls = ["http://www.appledaily.com.tw/realtimenews/section/new/1"]
    visited_url = []

    def parse(self, response):
        self.visited_url.append(response._url)
        domain = "http://www.appledaily.com.tw"
        soup = BeautifulSoup(response.body, 'html.parser')
        for new in soup.select('.rtddt'):
            yield scrapy.Request(domain+new.a['href'], callback=self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body,"html.parser")
        appitem = AppleItem()
        appitem['title']=res.select('#h1')[0].text
        appitem['content'] = res.select('#summary')[0].text
        appitem['time'] = res.select('time')[0].text
        # print(res.select("#h1")[0].text)
        return appitem