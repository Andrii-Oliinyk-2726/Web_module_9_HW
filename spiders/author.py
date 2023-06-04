import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response, *args):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "fullname": quote.xpath("span/small/text()").get(),
                "born_date": response.css("p.author-born-date::text").get(),
                "born_location": quote.xpath("span/small/text()").extract(),
                "description": quote.xpath("span/small/text()").extract(),
            }
            # "born_date": quote.xpath("span/a/@href").get(),
            # "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
            # "author": quote.xpath("span/small/text()").extract(),
            # "quote": quote.xpath("span[@class='text']/text()").get()
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
