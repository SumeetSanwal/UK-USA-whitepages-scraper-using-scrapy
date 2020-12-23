# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import pandas as pd

class UkPipeline:
    def process_item(self, item, spider):
        # df = pd.DataFrame(list(zip(item['name'], item['num'])))
        # df['Address'] = item['address']
        # TO REPLACE ALL '-' IN THE NUMBERS
        # df.replace(r"-", '', regex=True, inplace=True)
        # df2 = pd.concat(lt, axis=0, ignore_index=True)
        # # df2.to_csv(r"out.csv", sep=',', index=None, header=None)
        df=pd.DataFrame(item['name'])
        df2=pd.DataFrame(item['num'])
        df3=pd.DataFrame(item['address'])
        df2.drop_duplicates(inplace=True)
        # df['num'] = item['num']
        # df['Address'] = item['address']
        # if file does not exist write header
        if not os.path.isfile('name.csv'):
            df.to_csv(r'name.csv', index=None, header=None)
        else:  # else it exists so append without writing the header
            df.to_csv(r'name.csv', mode='a', index=None, header=None)

        if not os.path.isfile('num.csv'):
            df2.to_csv(r'num.csv', index=None, header=None)
        else:  # else it exists so append without writing the header
            df2.to_csv(r'num.csv', mode='a', index=None, header=None)

        if not os.path.isfile('address.csv'):
            df3.to_csv(r'address.csv', index=None, header=None)
        else:  # else it exists so append without writing the header
            df3.to_csv(r'address.csv', mode='a', index=None, header=None)


        return item
