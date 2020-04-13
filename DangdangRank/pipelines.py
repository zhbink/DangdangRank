# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.pipelines.images import ImagesPipeline


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db, mongo_col):
        self.mongo_uri = mongo_url
        self.mongo_db = mongo_db
        self.mongo_col = mongo_col

    # from_crawler()方法是一个类方法，用@classmethod标识，是一种依赖注入的方式。
    # 它的参数是crawler，通过crawler对象，我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息，然后创建一个Pipeline实例。
    # 参数cls就是Class，最后返回一个Class实例。
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # 服务器url+port
            mongo_url=crawler.settings.get('MONGO_URL'),
            # 库
            mongo_db=crawler.settings.get('MONGO_DB'),
            # 集合
            mongo_col=crawler.settings.get('MONGO_COL')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.col = self.db[self.mongo_col]

    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict.pop('front_image_url')
        self.col.insert_one(item_dict)
        return item

    def close_spider(self, spider):
        self.client.close()


class BookImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            image_file_path = ""
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path
        item["front_image_url"] = item["front_image_url"][0]
        return item
