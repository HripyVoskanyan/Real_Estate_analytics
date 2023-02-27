import requests
from bs4 import BeautifulSoup
from config import *


def create_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(config['main'][0], attrs={'class': config['main'][1]})
    return results


def collect_address(results):
    for row in results:
        try:
            temp = row.find(config['address'][0], attrs={
                'class': config['address'][1]}).text.replace('\n', "")
            return temp

        except:
            pass
    return None


def collect_sqm(results):
    for row in results:
        try:
            temp = row.find(config['sqm'][0], attrs={
                'class': config['sqm'][1]}).text.replace(
                '\n', "")
            return temp
        except:
            pass
    return None


def collect_info(results):
    for row in results:
        try:
            temp = row.find(config['info'][0], attrs={
                'class': config['info'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_price(results):
    for row in results:
        try:
            temp = row.find(config['price'][0], attrs={
                'class': config['price'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_more(results):
    for row in results:
        try:
            temp = row.find(config['more'][0], attrs={
                'class': config['more'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_views(results):
    for row in results:
        try:
            temp = row.find(config['views'][0], attrs={
                'class': config['views'][1]}).text
            return temp
        except:
            pass
    return None


def collect_data_lat(results):
    for row in results:
            try:
                temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lat']
                return temp

            except:
                pass
    return None


def collect_data_lng(results):
    for row in results:
            try:
                temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lng']
                return temp

            except:
                pass
    return None


def collect_all(results, df):
    app = {'address': collect_address(results), 'sqm': collect_sqm(results),
           'info': collect_info(results), 'price': collect_price(results),
           'more': collect_more(results), 'views': collect_views(results),
           'data-lat': collect_data_lat(results), 'data-lng': collect_data_lng(results)}
    df = df.append(app, ignore_index=True)
    return df
