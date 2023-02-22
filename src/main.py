import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

main_tag = 'item'
url0 = 'https://myrealty.am/en/bnakaranneri-vacharq/7784'
keyword = "bedroom"
mainpage = 'https://myrealty.am/en/apartments-for-sale/Yerevan/7762'
pagenum = 58


def get_pages(mainpage, pagenum):
    pages = []
    for i in range(2, pagenum):
        pages.append(f"{mainpage}+'?page={i}")
    return pages


def get_links(url, main_tag, keyword):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('div', attrs={'class': f'{main_tag}'})
    links = []
    for link in soup.find_all('a',
                              attrs={'href': re.compile(keyword)}):
        links.append(link.get('href'))
    return links


config = {'main': 'container',
          'address': 'col-auto item-view-address d-none d-xl-block mr-0',
          'sqm': 'col-12 d-flex justify-content-between justify-content-sm-start item-view-price-params',
          'info': 'item-view-title',
          'price': 'item-view-price',
          'more': 'item-view-list-params',
          'facilities': 'row item-view-facilities mb-4',
          'additional': 'row item-view-facilities mb-4',
          'views': 'item-view-count',
          'coord': 'row no-gutters mb-4'
          }


def get_apartments(links, config):
    apparts = []
    for url in links:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('div', attrs={'class': config['main']})
        for row in results:
            app = {}
            try:
                app['address'] = row.find('div', attrs={
                    'class': config['address']}).text.replace('\n', "")
            except:
                app['address'] = row.find('div', attrs={
                    'class': config['address']})
            try:
                app['sqm'] = row.find('div', attrs={
                    'class': config['sqm']}).text.replace(
                    '\n', "")
            except:
                app['sqm'] = row.find('div', attrs={
                    'class': config['sqm']})
            try:
                app['info'] = row.find('h1', attrs={
                    'class': config['info']}).text.replace('\n', "")
            except:
                app['info'] = row.find('div', attrs={
                    'class': config['info']})
            try:
                app['price'] = row.find('div', attrs={
                    'class': config['price']}).text.replace('\n', "")
            except:
                app['price'] = row.find('div', attrs={
                    'class': config['price']})
            try:
                app['more'] = row.find('ul', attrs={
                    'class': config['more']}).text.replace('\n', "")
            except:
                app['more'] = row.find('ul', attrs={
                    'class': config['more']})
            try:
                a = row.find('div', attrs={
                    'class': config['facilities']}).findAll('li')
                some_string = ""
                for li in a:
                    some_string += (li.get_text() + "--")
                app['facilities'] = some_string + '\n'

            except:
                app['facilities'] = ' '
            try:
                a = row.findAll('div', attrs={
                    'class': config['additional']})[1].findAll('li')
                some_string = ""
                for li in a:
                    some_string += (li.get_text() + "--")
                app['additional info'] = some_string + '\n'
            except:
                app['additional info'] = ' '
            try:
                app['views'] = row.find('span', attrs={
                    'class': config['views']}).text
            except:
                app['views'] = row.find('span', attrs={
                    'class': config['views']})
            try:
                app['coord'] = row.find("div", attrs={
                    "class": 'row no-gutters mb-4'
                })['data-lat'].text
            except:
                app['coord'] = row.findAll(attrs={
                    "data-lat": True, "data-lng": True})

            apparts.append(app)
    df = pd.DataFrame.from_records(apparts)
    df = df.dropna(subset=['address'])
    return df


pages = get_pages(mainpage, pagenum)
links = []
for i in pages:
    links = links + get_links(url0, main_tag, keyword)
df = get_apartments(links, config)
df.to_excel('C:\AUA\Capstone\code\data\df.xlsx')
