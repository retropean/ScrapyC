from scrapy.spider import Spider
from scrapy.selector import Selector
from lxml import html, etree
from locspider.items import LocspiderItem

import datetime
import time
import sys
if sys.version_info[0] >= 3:
    unicode = str

class LocSpider(Spider):
	name = "locspider"
	allowed_domains = ["craigslist.org/about/sites"]
	start_urls = ["https://www.craigslist.org/about/sites"]

	def __init__(self):
		Spider.__init__(self)
		
	def __del__(self):
		Spider.__del__(self)

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//section[@class="body"]')
		items = []
		co,st,ci,divacounter,divbcounter = 1,1,1,1,1

		for site in sites:
			while map(unicode.strip, site.xpath('.//div[@class="colmask"][last()+1]/div[last()+1]/ul[last()+1]/li[last()+1]/a/text()'.format(j=ci, e=divacounter, k=divbcounter)).extract()) != map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st, e=divacounter, k=divbcounter)).extract()):
				while map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[last()+1]/ul[last()+1]/li[last()+1]/a/text()'.format(j=ci, e=divacounter, k=divbcounter)).extract()) != map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st, e=divacounter, k=divbcounter)).extract()):	
					#get all objects within one div tag (first row of states)
					while map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[last()+1]/li[last()+1]/a/text()'.format(j=ci, e=divacounter, k=divbcounter)).extract()) != map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st, e=divacounter, k=divbcounter)).extract()):
						#get all objects within one ul tag
						while map(unicode.strip, site.xpath('//ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st)).extract()) != map(unicode.strip, site.xpath('//ul[{f}]/li[last()+1]/a/text()'.format(f=st)).extract()):
							item = LocspiderItem()
							item['city'] = map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[{f}]/li[{j}]/a/text()'.format(j=ci, f=st, e=divacounter, k=divbcounter)).extract())
							item['domain'] = map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/ul[{f}]/li[{j}]/a/@href'.format(j=ci, f=st, e=divacounter, k=divbcounter)).extract())
							item['state'] = map(unicode.strip, site.xpath('.//div[@class="colmask"][{e}]/div[{k}]/h4[{i}]/text()'.format(i = st, e=divacounter, k=divbcounter)).extract())
							item['continent'] = map(unicode.strip, site.xpath('.//h1[{i}]/text()'.format(i = co)).extract())
							ci+=1
							items.append(item)
						st+=1
						ci=1
					divbcounter+=1
					ci=1
					st=1
				divacounter+=1
				divbcounter=1
				co+=1
		return items