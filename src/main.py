import pandas as pd
from collect_urls import *
from collect_information import *
import os
import time
from assets.config1 import *
from assets.config2 import *
from assets.config_rent1 import *
from assets.config_rent2 import *

try:
    os.remove("urls.txt")
except:
    pass


# all_urls = get_all_urls(sitemap_url)
# write_in_file(all_urls)
df = pd.DataFrame()
with open("item_urls.txt", "r") as f:
    for url0 in f:
        print(url0)
        url0 = url0.replace(" ", "")
        url0 = url0.replace("\n", "")
        df = collect_all(create_soup(url0, config), df, config)
        time.sleep(3)
df.to_csv("C:\AUA\Capstone\code\data\data_new1.csv")


"""
try:
    print("start")
    os.remove('urls.txt')
except:
    pass
print('getting pages')
get_pages(mainpage2, pagenum2, main_tag2, keyword2, sign2, class_2)
print("df")
df = pd.DataFrame()
print("opening url")
with open('urls.txt', 'r') as f:
    for url0 in f:
        print(url0)
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0, config2), df, config2)
        time.sleep(3)
df.to_excel('C:\AUA\Capstone\code\data\df2.xlsx')

"""
"""
# rent1
try:
    os.remove('urls.txt')
except:
    pass
get_pages(mainpage3, pagenum3, main_tag3, keyword3, sign3, class_3)
df = pd.DataFrame()
with open('urls.txt', 'r') as f:
    for url0 in f:
        print(url0)
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0, config3), df, config3)
df.to_excel('C:\AUA\Capstone\code\data\df_rent1.xlsx')
"""
"""
# rent2
try:
    os.remove('urls.txt')
except:
    pass
get_pages(mainpage4, pagenum4, main_tag4, keyword4, sign4, class_4)
df = pd.DataFrame()
with open('urls.txt', 'r') as f:
    for url0 in f:
        print(url0)
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0, config4), df, config4)
        time.sleep(4)
df.to_excel('C:\AUA\Capstone\code\data\df_rent2.xlsx')
"""
