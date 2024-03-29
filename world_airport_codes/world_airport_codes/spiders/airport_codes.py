# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html']
    start_urls = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html']

    def parse(self, response):
        data=[]
        table = response.css('.stack2')
        row_selector =  ".//tr[@class='light-row'] | .//tr[@class='dark-row']"
        for row in table.xpath(row_selector):
            nama = row.xpath('./th/a/text()').extract_first()
            type = row.xpath('./td[1]/text()[2]').extract_first().strip()
            city = row.xpath('./td[2]/text()').extract_first()
            country = row.xpath('./td[3]/text()').extract_first()
            iata = row.xpath('./td[4]/text()').extract_first()
            icao = row.xpath('./td[5]/text()').extract_first()
            iaa = row.xpath('./td[6]/text()').extract_first()

            data.append({
            'nama :' : nama,
            'type :' : type,
            'city :' : city,
            'country :': country,
            'iata :': iata,
            'icao :': icao,
            'iaa :': iaa
            })
        return data
