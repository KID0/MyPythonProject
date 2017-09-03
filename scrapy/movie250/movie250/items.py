import scrapy

# 搞了一个新class，scrapy.Field()是标准写法，不用考虑太多
class Movie250Item(scrapy.Item):
	# 以下是各种项目
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()