import scrapy

from pep_parse.constants import PEP_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        pep_links = response.css(
            ('section[id="numerical-index"] '
             'a.pep.reference.internal::attr(href)')
        ).getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get().split('–')
        data = dict(
            number=pep_title[0].strip(),
            name=pep_title[1].strip(),
            status=response.css('dt:contains("Status") + dd abbr::text').get()
        )
        yield PepParseItem(data)
