import scrapy


class UkSchoolsSpider(scrapy.Spider):
    name = "UK_schools"
    allowed_domains = ["4icu.org"]
    start_urls = ["https://www.4icu.org/gb/a-z/"]

    def parse(self, response):
        # extracting the list of university elements
        universities = response.xpath('//tr')

        for uni in universities:
            # extracting the link and the name
            link = uni.xpath('.//td[2]/a/@href').get()
            name = uni.xpath('.//td[2]/a/text()').get()

            yield {
                'name': name,
                'link': link
            }
