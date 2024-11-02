import scrapy
from scrapy.http import Response

domain = 'example-website-with-coloring-pages-for-kids.com'


# see https://docs.scrapy.org/en/latest/topics/practices.html?highlight=user%20agent#avoiding-getting-banned

class BlogSpider(scrapy.Spider):
    name = 'spider'
    start_urls = [f'https://{domain}/']
    allowed_domains = [domain]

    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
    }

    # noinspection PyMethodOverriding
    def parse(self, response: Response):
        for link in response.css('a::attr(href)').extract():
            if '.pdf' in link:
                yield {'pdf_url': response.urljoin(link)}
        for next_page in response.css('a'):
            if follow_link(next_page):
                yield response.follow(next_page, self.parse)


def follow_link(next_page):
    href = next_page.attrib['href']
    return not (href.startswith('mailto:') or '.pdf' in href)
