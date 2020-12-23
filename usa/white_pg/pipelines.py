# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import pandas as pd

class AnywhoPipeline:
    def process_item(self, item, spider):
        df=pd.DataFrame(list(zip(item['num'],item['age'])))


        if not os.path.isfile('..\..\..\..\Data.csv'):
            df.to_csv(r'..\..\..\..\Data.csv',index=None,header=None)
        else:  # else it exists so append without writing the header
            df.to_csv(r'..\..\..\..\Data.csv', mode='a',index=None,header=None)


        return item
