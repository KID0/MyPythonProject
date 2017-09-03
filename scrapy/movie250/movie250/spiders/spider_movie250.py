import scrapy
# 这里记得引入这个类
from movie250.items import Movie250Item

class Movie250Spider(scrapy.Spider):
  """docstring for Movie250Spider"""
  # 这个'name'才是我们启动spider的名字
  name = 'movie250'
  allowed_domains = ["douban.com"]
  start_urls = [
    "http://movie.douban.com/top250/"
  ]

  def parse(self, response):
    for info in response.xpath('//div[@class="item"]'):
      # Movie250Item()在items.py中自行创立，直接引用即可
      item = Movie250Item()
      # 下面就是一个字典了
      # 不管是文字还是属性通通要使用extract()方法才能取得（前面是找到，后面是取出）
      item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
      item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
      item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
      item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
      item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
      item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
      # 这个yield很棒！
      yield item

    # 翻页
    next_page = response.xpath('//span[@class="next"]/a/@href')
    if next_page:
      # next_page是含有一个项目的list，所以用[0]
      # 别忘了extract()方法
      # response就是"http://movie.douban.com/top250/"
      url = response.urljoin(next_page[0].extract())
      # 产生一个request
      yield scrapy.Request(url, self.parse)