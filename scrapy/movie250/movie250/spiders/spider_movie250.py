import scrapy
from movie250.items import Movie250Item

class Movie250Spider(scrapy.Spider):
  """docstring for Movie250Spider"""
  name = 'movie250'
  allowed_domains = ["douban.com"]
  start_urls = [
    "http://movie.douban.com/top250/"
  ]

  def parse(self, response):
    for info in response.xpath('//div[@class="item"]'):
      item = Movie250Item()
      item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
      item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
      item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
      item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
      item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
      item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
      yield item

    # 翻页
    next_page = response.xpath('//span[@class="next"]/a/@href')
    if next_page:
      # next_page是含有一个项目的list，所以用[0]
      url = response.urljoin(next_page[0].extract())
      yield scrapy.Request(url, self.parse)