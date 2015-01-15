from scrapy.item import Item, Field

class CLItem(Item):
	title = Field()
	price = Field()
	location = Field()
	postdate = Field()
	odometer = Field()
	color = Field()
	transmission = Field()
	title = Field()
	cylinders = Field()
	drive = Field()
	fuel = Field()
	type = Field()
	datescraped = Field()
	urlscraped = Field()	
pass