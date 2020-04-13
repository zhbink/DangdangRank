# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Identity, Compose
from scrapy.loader import ItemLoader
from DangdangRank.utils.common import extract_num


def remove_sign(value):
    a = value.split('¥')[1]
    return value.split('¥')[1]


def remove_brackets(value):
    return re.sub("（.*）", "", value)


class DangdangItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DangdangItem(scrapy.Item):
    url = scrapy.Field()
    # url_object_id = scrapy.Field()
    rank_year = scrapy.Field(
        input_processor=Compose(
            lambda x: int(x[0])
        )
    )
    rank = scrapy.Field(
        input_processor=Compose(
            lambda x: x[0],
            lambda x: int(x.split('.')[0]),
        )
    )
    book_name = scrapy.Field(
        # input_processor=MapCompose(remove_brackets)
        input_processor=Compose(
            lambda x: x[0],
            lambda x: re.sub("\（.*", "", x),
            lambda x: re.sub("\(.*", "", x)
        )
    )
    author = scrapy.Field()
    publisher = scrapy.Field(
        input_processor=Compose(
            lambda x: x[-1]
        )
    )
    price = scrapy.Field(
        # input_processor=MapCompose(remove_sign)
        input_processor=Compose(
            lambda x: x[0],
            lambda x: float(x.split('¥')[1])
        )
    )
    publish_time = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=Identity()
    )
    front_image_path = scrapy.Field()
    comment_nums = scrapy.Field(
        input_processor=MapCompose(extract_num)
    )
    recommend_percent=scrapy.Field(
        input_processor=Compose(
            lambda x: x[0],
            lambda x: float(x.split('%')[0])
        )
    )
