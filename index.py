import scrapy

class WebSpider(scrapy.Spider):
  name = "web_spider"
  start_urls = ['https://brickset.com/sets/year-2016']
  user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

  def parse(self, response):
    SET_SELECTOR = '.set'
    for brickset in response.css(SET_SELECTOR):

      NAME_SELECTOR = 'h1 a ::text'
      PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
      MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
      IMAGE_SELECTOR = 'img ::attr(src)'
      yield {
          'name': brickset.css(NAME_SELECTOR).extract_first(),
          'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
          'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
          'image': brickset.css(IMAGE_SELECTOR).extract_first(),
      }