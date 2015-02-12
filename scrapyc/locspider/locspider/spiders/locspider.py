from scrapy.spider import Spider
from scrapy.selector import Selector
from lxml import html, etree
from items import LocspiderItem

import datetime
import time

class LocSpider(Spider):
	name = "locspider"
#	download_delay = 2
	allowed_domains = ["http://www.craigslist.org/about/sites"]
	start_urls = ["http://www.craigslist.org/about/sites"]

	def __init__(self):
		Spider.__init__(self)
		
	def __del__(self):
		Spider.__del__(self)

	def parse(self, response):
		sel = Selector(response)
#		sites = sel.xpath('//div/ul/li')
#		sites = sel.xpath('//section[@class="body"]/h1')
		sites = sel.xpath('//section[@class="body"]')
		items = []
		co = 1
		st = 1
		ci = 1
		
		for site in sites:
			while map(unicode.strip, site.xpath('//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract()) != map(unicode.strip, site.xpath('//ul[last()]/li[last()]/a/text()'.format(f=st)).extract()):
				while map(unicode.strip, site.xpath('//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract()) != map(unicode.strip, site.xpath('//ul[{f}]/li[last()]/a/text()'.format(f=st)).extract()):
					item = LocspiderItem()
					item['city'] = map(unicode.strip, site.xpath('.//div[3]/div/ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract())
					item['domain'] = map(unicode.strip, site.xpath('.//div[3]/div/ul[{f}]/li[{j}]/a/@href'.format(j=ci, f=st)).extract())
					item['state'] = map(unicode.strip, site.xpath('.//div[3]/div/h4[{i}]/text()'.format(i = st)).extract())
					item['continent'] = map(unicode.strip, site.xpath('.//div[3]/div/h1[{i}]/text()'.format(i = co)).extract())
					ci+=1
					items.append(item)
				st+=1
				ci=1
			co+=1
			st=1
		return items
'''				
		for site in sites:
			while map(unicode.strip, site.xpath('//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract()) != map(unicode.strip, site.xpath('//ul[last()]/li[last()]/a/text()'.format(f=st)).extract()):
				while map(unicode.strip, site.xpath('//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract()) != map(unicode.strip, site.xpath('//ul[{f}]/li[last()]/a/text()'.format(f=st)).extract()):
					item = LocspiderItem()
					item['city'] = map(unicode.strip, site.xpath('.//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract())
					item['domain'] = map(unicode.strip, site.xpath('.//ul[{f}]/li[{j}]/a/@href'.format(j=ci, f=st)).extract())
					item['state'] = map(unicode.strip, site.xpath('.//h4[{i}]/text()'.format(i = st)).extract())
					item['continent'] = map(unicode.strip, site.xpath('.//h1[{i}]/text()'.format(i = co)).extract())
					ci+=1
					items.append(item)
				st+=1
				ci=1
			co+=1
			st=1
		return items
'''