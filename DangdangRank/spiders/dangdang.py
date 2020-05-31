# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from DangdangRank.items import DangdangItemLoader, DangdangItem
from DangdangRank.utils.common import get_md5
from DangdangRank.settings import RANK_YEAR
import requests
import urllib


# scrapy shell -s USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36" http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2016-0-1-1

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['product.dangdang.com', 'bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/']
    rank_year = RANK_YEAR

    def parse(self, response):
        for i in range(1, 26):
            url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-{0}-0-1-{1}'.format(self.rank_year, i)
            yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        for r in response.css(".bang_list li"):
            loader = DangdangItemLoader(DangdangItem(), selector=r)
            loader.add_value("rank_year", self.rank_year)
            loader.add_css("rank", ".list_num::text")
            url = r.css(".name a::attr(href)").extract_first()
            loader.add_value("url", url)
            loader.add_value("id", get_md5(url)+self.rank_year)
            loader.add_css("book_name", ".name a::attr(title)")
            loader.add_css("author", ".publisher_info a::text")
            loader.add_css("publisher", ".publisher_info a::text")
            loader.add_css("price", ".price_r::text")
            publish_time = r.css(".publisher_info span::text").extract_first()
            if not publish_time:
                publish_time = "1970-01-01"
            loader.add_value("publish_time", publish_time)

            front_image_url = r.css(".pic img::attr(src)").extract_first()
            loader.add_value("front_image_url", front_image_url)
            loader.add_css("comment_nums", ".star a::text")
            loader.add_css("recommend_percent", ".tuijian::text")
            item = loader.load_item()
            yield item
