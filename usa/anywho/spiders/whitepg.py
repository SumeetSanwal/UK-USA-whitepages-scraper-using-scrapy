import scrapy
from urllib.parse import urljoin
from ..items import AnywhoItem

# from scraper_api import ScraperAPIClient
# client = ScraperAPIClient('a4c65599e7baf9daa10a218d1920f280')

class Whitepg(scrapy.Spider):
    name = 'sam'

    # start_url = ['']#ENTER START URL
    # headers={
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.9',
    #     'cache-control': 'max-age=0',
    #     'cookie': 'DG_ZID=4CBA3743-FF8F-3666-97BC-344CF1E0A2A8; DG_ZUID=AA1ACF23-6997-3552-88DF-E983FE6AC5E4; DG_HID=1CFF27C8-B64F-3BDF-97C5-63CDFB82A452; DG_SID=192.241.244.170:3bgXXHFBK/VHEYFmtPlQb1XyvMHtTD5OOl32PRaa+0o; visited_premium=true; wp_pid=WpxP7hHLHjFcmVPex9EoTg; com_whitepages_wp_beta=; com_whitepages_wp_app_vtwo=version_b; _hjid=79994c5d-4c57-4b10-b4ef-c09b55989612; shown_cookie_banner=true; device_id=461826b7-d3a3-416c-97fb-861f89996b1fR; amplitude_id_4452f969da1962f05527ab14f5db83dawhitepages.com=eyJkZXZpY2VJZCI6ImUwNjI3MGFhLWQxMGEtNDhkNy1hMzlmLWU0MTkyYTNiMTgwMlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMTI5OTIxNTAyMiwibGFzdEV2ZW50VGltZSI6MTYwMTI5OTIxNTAyMiwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; initial_referrer=; initial_referring_domain=; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_apiwhitepages.com=eyJkZXZpY2VJZCI6ImNiN2E4MWZkLTA5MjAtNDczNi1iNzVlLTkxNDA1YmQwZWY5N1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMTM5NDE2ODUzMCwibGFzdEV2ZW50VGltZSI6MTYwMTM5NDUwMDg0NSwiZXZlbnRJZCI6NjU3LCJpZGVudGlmeUlkIjo2NTcsInNlcXVlbmNlTnVtYmVyIjoxMzE0fQ==; DG_IID=03A70DD9-EFC3-3FD0-9C90-F5A327531603; DG_UID=A96EFA58-34B2-355D-91EE-D728BB4CFD31',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'same-origin',
    #     'sec-fetch-site': 'same-origin',
    #     'upgrade-insecure-requests':'1',
    #     'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    #
    # }

    def start_requests(self):
        yield scrapy.Request(url="https://thatsthem.com/phone/708",callback=self.parse)

    def parse(self, response):

        for href in response.css(".column-count-3 a::attr(href)"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url, callback=self.parse_city)

    # def parse_pagination(self,response):
    #     for href in response.css(".page a::attr(href)"):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url, headers=self.headers, callback=self.parse_city)

    def parse_city(self, response):
        for href in response.css(".column-count-4 a ::attr(href)"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url, callback=self.parse_person)

    def parse_person(self, response):
        items = AnywhoItem()
        num1 = response.css('.col-md-8 > span::text').extract()
        items['num'] = num1
        age1 = response.css(".ThatsThem-record-age .active ::text").extract()
        items['age'] = age1

        yield items

# THINGS TO ADD
# PAGINATION
# 1.headers
# 2.IP AND PROXY
# 3.PIPELINE
# NVI-NAME,ADDRESS
