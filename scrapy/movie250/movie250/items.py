import scrapy

class Movie250Item(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()