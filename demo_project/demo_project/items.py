# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

class JokeItem(scrapy.Item):
    # define the fields for your item here like:
    joke_text = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )

class AmazonItem(scrapy.Item):

    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )
    book_img_link = scrapy.Field()