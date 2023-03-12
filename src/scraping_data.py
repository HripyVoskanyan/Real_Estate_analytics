import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

url0 = 'https://myrealty.am/en/bnakaranneri-vacharq/7784'

page = requests.get(url0)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('div', attrs={'class': 'item'})
name = "^https://myrealty.am/en/2-bedroom/"
links = []
for link in soup.find_all('a',
                          attrs={'href': re.compile(name)}):
    # display the actual urls
    links.append(link.get('href'))
print(len(links))
apparts = []
for url in links:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('div', attrs={'class': 'container'})
    for row in results:
        app = {}
        try:
            app['address'] = row.find('div', attrs={
                'class': 'col-auto item-view-address d-none d-xl-block mr-0'}).text.replace('\n', "")
        except:
            app['address'] = row.find('div', attrs={'class': 'col-auto item-view-address d-none d-xl-block mr-0'})
        try:
            app['sqm'] = row.find('div', attrs={
                'class': 'col-12 d-flex justify-content-between justify-content-sm-start item-view-price-params'}).text.replace('\n', "")
        except:
            app['sqm'] = row.find('div', attrs={
                'class': 'col-12 d-flex justify-content-between justify-content-sm-start item-view-price-params'})
        try:
            app['info'] = row.find('div', attrs={
                'class': 'row item-view-information mb-4'}).text.replace('\n', "")
        except:
            app['info'] = row.find('div', attrs={'class': 'row no-gutters align-items-center'})
        try:
            app['price'] = row.find('div', attrs={
                'class': 'item-view-price'}).text.replace('\n', "")
        except:
            app['price'] = row.find('div', attrs={'class': 'item-view-price'})
        try:
            app['more'] = row.find('ul', attrs={
                'class': 'item-view-list-params'}).text.replace('\n', "")
        except:
            app['more'] = row.find('div', attrs={
                'class': 'col-lg-12 col-xl-4 mb-2'})
        try:
            a = row.find('div', attrs={
                'class': 'row item-view-facilities mb-4'})
            b = a.find('div', attrs={
                'class': 'col-12'})
            some_ul = b.findAll('ul', attrs={
                'class': 'row'})[0].findAll('li')
            some_string = ""
            for li in some_ul:
                some_string += (li.get_text() + "--")
            app['facilities'] = some_string + '\n'

        except:
            app['facilities'] = row.find('div', attrs={
                'class': 'row item-view-facilities mb-4'})
        try:
            app['additional info'] =  row.findAll('div', attrs={
                'class': 'row item-view-facilities mb-4'})[1].text
        except:
            app['additional info'] = row.find('span', attrs={
                'class': 'item-view-additional-icon kahuyq'})
        try:
            app['views'] = row.find('span', attrs={
                'class': 'item-view-count'}).text
        except:
            app['views'] = row.find('span', attrs={
                'class': 'item-view-count'})
        try:
            app['coord'] = row.find("div", attrs = {
                "class": 'row no-gutters mb-4'
            })['data-lat'].text
        except:
            app['coord'] = row.findAll(attrs={
                "data-lat": True, "data-lng": True})


        apparts.append(app)
df = pd.DataFrame.from_records(apparts)
df = df.dropna(subset = ['address'])
#df = df.drop_duplicates()
df = df.reset_index()
#df = df.drop_duplicates()
df.to_excel('C:\AUA\Capstone\code\data\df.xlsx')
print(df)