# -*- coding: utf-8 -*-
import scrapy
from image.items import ImageItem

class MyimageSpider(scrapy.Spider):
    name = "myimage"
    allowed_domains = ["https://book.douban.com/"]
    start_urls = (
        'https://book.douban.com/',
    )

    def parse(self, response):
        item = ImageItem()
        item['image_urls'] = response.xpath('//div[@class="carousel"]//div[@class="cover"]//img/@src').extract()
        return item