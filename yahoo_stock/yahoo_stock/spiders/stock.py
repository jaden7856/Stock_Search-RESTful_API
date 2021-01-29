import scrapy
import re
from yahoo_stock.items import YahooStockItem
import cgi


# # 웹 검색한 text
# form = cgi.FieldStorage()
# symbol_name = form.getvalue('symbol')
symbol_name = 'AAPL'

def symbol_edit(nam: str) -> str:
    sym = re.search(r'\([^)]*\)', str(nam))
    symbol = sym.group(0).replace('(', '').replace(')', '')
    return symbol


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['yahoo.com']

    URL = 'https://finance.yahoo.com/quote/%s?p=%s'
    start_urls = [URL % (symbol_name, symbol_name)]

    def parse(self, response):
        nam = response.xpath("//*[@id='quote-header-info']/div[2]/div[1]/div[1]/h1/text()").extract()
        symbols = symbol_edit(nam)
        names = nam[0].split(' (')[0]
        prices = response.xpath("//*[@id='quote-header-info']/div[3]/div[1]/div/span[1]/text()")[0].extract()
        opens = response.xpath("//*[@id='quote-summary']/div[1]/table/tbody/tr[2]/td[2]/span/text()")[0].extract()
        min_max = response.xpath("//*[@id='quote-summary']/div[1]/table/tbody/tr[5]/td[2]/text()").extract()
        day_mins = min_max[0].split(' -')[0]
        day_maxs = min_max[0].split('- ')[1]
        volumes = response.xpath("//*[@id='quote-summary']/div[1]/table/tbody/tr[7]/td[2]/span/text()")[0].extract()
        modify_dates = response.xpath("//*[@id='quote-market-notice']/span/text()")[0].extract()

        item = YahooStockItem()
        item['symbol'] = symbols
        item['name'] = names
        item['price'] = prices
        item['open'] = opens
        item['day_min'] = day_mins
        item['day_max'] = day_maxs
        item['volume'] = volumes
        item['modify_date'] = modify_dates

        return item
