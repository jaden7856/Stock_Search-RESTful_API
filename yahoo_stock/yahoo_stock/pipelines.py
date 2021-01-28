import sqlite3
from scrapy.exporters import JsonItemExporter
import os


class YahooStockPipeline(object):

    def __init__(self):
        self.con = sqlite3.connect(
            os.path.abspath('C:/Users/User/Desktop/DataStudy/Project/django_stock_web/db.sqlite3'))
        self.cur = self.con.cursor()

        # self.createTable()

    # def createTable(self):
    #     self.cur.execute('''CREATE TABLE IF NOT EXISTS blog_post(
    #     symbol TEXT PRIMARY KEY, name TEXT, price TEXT, open TEXT, day_min TEXT, day_max TEXT,
    #     volume TEXT, modify_date TEXT)''')

    # Data processing
    def process_item(self, item, spider):
        self.storeInDb(item)
        spider.logger.info('Item to DB inserted.')

        return item

    def storeInDb(self, item):
        values = zip([item['symbol']], [item['name']], [item['price']], [item['open']], [item['day_min']],
                     [item['day_max']], [item['volume']], [item['modify_date']])

        self.cur.executemany('''INSERT OR REPLACE INTO blog_post(symbol, name, price, open, day_min, day_max, volume, modify_date) 
                             VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', values)

        self.con.commit()
        # Close the database
        self.con.close()


class JsonPipeline(object):
    def __init__(self):
        self.file = open("stock.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
