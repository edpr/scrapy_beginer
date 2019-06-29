# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['https://www.world-airport-codes.com/alphabetical/airport-code/a.html?page=1']
    start_urls = ['https://www.world-airport-codes.com/alphabetical/airport-code/a.html?page=1']

    def parse(self, response):
        data=[]

        data.append({
            'nama :':'CGK'
        })
        return data
