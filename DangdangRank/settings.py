# -*- coding: utf-8 -*-

# Scrapy settings for DangdangRank project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os


BOT_NAME = 'DangdangRank'

SPIDER_MODULES = ['DangdangRank.spiders']
NEWSPIDER_MODULE = 'DangdangRank.spiders'


ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
COOKIES_DEBUG = False
# DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    'DangdangRank.middlewares.RandomUserAgentMiddlware': 2,
    # 'DangdangRank.middlewares.ProxyMiddleware': 3,
}

ITEM_PIPELINES = {
# 'DangdangRank.pipelines.BookImagePipeline': 1,
    'DangdangRank.pipelines.MongoPipeline': 100,
    # 'DangdangRank.pipelines.RedisPipeline': 400,
}

custom_settings = {
    "COOKIES_ENABLED": False,
    'DEFAULT_REQUEST_HEADERS': {
        'Host': 'book.douban.com',
        'Origin': 'https://book.douban.com',
        'Referer': 'https://book.douban.com/',
    }
}

# 设置爬取年份
RANK_YEAR = '2017'

""" mongodb相关设置 """
MONGO_URL = 'localhost:27017'
#MONGO_URI = 'localhost:27017'
MONGO_DB = 'DjangoServer'
MONGO_COL = 'dangdangBook2'
MONGO_USER = 'user1'
MONGO_PASSWORD = 'MongoPassWd1'
SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"


""" middlewares 相关设置 """
RANDOM_UA_TYPE = "random"
IMAGES_URLS_FIELD = "front_image_url"
project_dir = os.path.dirname(os.path.abspath(__file__))
IMAGES_STORE = os.path.join(project_dir, 'images')
