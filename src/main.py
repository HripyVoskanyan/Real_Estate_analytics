import pandas as pd
from collect_urls import *
from collect_information import *

get_pages(mainpage, pagenum, main_tag, keyword)
df = pd.DataFrame()
with open('urls.txt', 'r') as f:
    for url0 in f:
        url0 = url0.replace(' ', '')
        url0 = url0.replace('\n', '')
        df = collect_all(create_soup(url0), df)
df.to_excel('C:\AUA\Capstone\code\data\df.xlsx')
