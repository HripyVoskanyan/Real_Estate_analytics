import requests
from bs4 import BeautifulSoup


def create_soup(url, config):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(config['main'][0], attrs={'class': config['main'][1]})
    return results


def collect_address(results, config):
    for row in results:
        try:
            temp = row.find(config['address'][0], attrs={
                'class': config['address'][1]}).text.replace('\n', "")
            return temp

        except:
            pass
    return None


def collect_sqm(results, config):
    for row in results:
        try:
            temp = row.findAll(config['sqm'][0], attrs={
                'class': config['sqm'][1]})[config['sqm'][2]].text.replace('\n', "")
            return temp

        except:
            pass
    return None


def collect_rooms(results, config):
    for row in results:
        try:
            temp = row.findAll(config['rooms'][0], attrs={
                'class': config['rooms'][1]})[config['rooms'][2]].text.replace('\n', "")
            return temp

        except:
            pass
    return None


def collect_floor(results, config):
    for row in results:
        try:
            temp = row.findAll(config['floor'][0], attrs={
                'class': config['floor'][1]})[config['floor'][2]].text.replace('\n', "").replace(' ', '')
            return temp

        except:
            pass
    return None


def collect_info(results, config):
    for row in results:
        try:
            temp = row.find(config['info'][0], attrs={
                'class': config['info'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_price(results, config):
    for row in results:
        try:
            temp = row.find(config['price'][0], attrs={
                'class': config['price'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_more(results, config):
    for row in results:
        try:
            temp = row.find(config['more'][0], attrs={
                'class': config['more'][1]}).text.replace('\n', "")
            return temp
        except:
            pass
    return None


def collect_views(results, config):
    for row in results:
        try:
            temp = row.find(config['views'][0], attrs={
                'class': config['views'][1]}).text
            return temp
        except:
            pass
    return None


def collect_data_lat(results, config):
    for row in results:
            try:
                temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lat']
                return temp

            except:
                pass
    return None


def collect_data_lng(results, config):
    for row in results:
            try:
                temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lng']
                return temp

            except:
                pass
    return None


def collect_additional(results, config):
    for row in results:
            try:
                temp = row.findAll(config['additional'][0], attrs={
                    'class': config['additional'][1]})[1].findAll(config['additional'][2])
                some_string = ""
                for li in temp:
                    some_string += (li.get_text() + '--')

                return some_string + '\n'
            except:
                pass
    return None

def collect_additional0(results, config):
    for row in results:
            try:
                temp = row.findAll(config['additional'][0], attrs={
                    'class': config['additional'][1]})[0].findAll(config['additional'][2])
                some_string = ""
                for li in temp:
                    some_string += (li.get_text() + '--')

                return some_string + '\n'
            except:
                pass
    return None


def collect_facilities(results, config):
    for row in results:
            try:
                temp = row.find(config['facilities'][0], attrs={
                    'class': config['facilities'][1]}).findAll(config['facilities'][2])
                some_string = ""
                for li in temp:
                    some_string += (li.get_text() + '--')

                return some_string + '\n'
            except:
                pass
    return None


def collect_all(results, df, config):
    app = {'address': collect_address(results, config), 'sqm': collect_sqm(results, config),
           'rooms': collect_rooms(results, config), 'floor': collect_floor(results, config),
           'info': collect_info(results, config), 'price': collect_price(results, config),
           'more': collect_more(results, config), 'views': collect_views(results, config),
           'additional': collect_additional(results, config), 'additional0': collect_additional0(results, config),
           'facilities': collect_facilities(results, config),
           'data-lat': collect_data_lat(results, config), 'data-lng': collect_data_lng(results, config)}
    df = df.append(app, ignore_index=True)
    return df
