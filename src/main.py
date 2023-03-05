import pandas as pd
from collect_urls import *
from collect_information import *
import os
from config1 import *
from config2 import *

try:
    os.remove('urls.txt')
except:
    pass

'''
get_pages(mainpage, pagenum, main_tag, keyword, sign, clas_)
df = pd.DataFrame()
with open('urls.txt', 'r') as f:
    for url0 in f:
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0, config), df, config)
df.to_excel('C:\AUA\Capstone\code\data\df.xlsx')
'''
get_pages(mainpage2, pagenum2, main_tag2, keyword2, sign2, class_2)
df = pd.DataFrame()
with open('urls.txt', 'r') as f:
    for url0 in f:
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0, config2), df, config2)
df.to_excel('C:\AUA\Capstone\code\data\df2.xlsx')

