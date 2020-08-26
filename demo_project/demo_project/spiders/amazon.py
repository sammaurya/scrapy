import scrapy
from ..items import AmazonItem
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/gp/bestsellers/books/?ie=UTF8&ref_=sv_ba_3'
    ]

    def parse(self, response):

        items = AmazonItem()
        for book in response.css('.zg-item-immersion'):

            book_name = book.css('.a-link-normal .zg-text-center-align').css(".a-section img::attr('alt')").extract_first()
            book_author = book.css('.a-link-normal+ .a-size-small .a-size-small').css('::text').extract_first()
            book_price = book.css('.p13n-sc-price').css('::text').extract_first()
            book_img_link = book.css('.a-spacing-small img::attr("src")').extract_first()

            items['book_name'] = book_name
            items['book_author'] = book_author
            items['book_price'] = book_price
            items['book_img_link'] = book_img_link

            yield items
        