import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET


def get_soup(url_str):
    urlopen = requests.get(url_str).text
    soup = BeautifulSoup(urlopen, 'lxml')
    return soup


def get_search_urls(soup):
    urls = set()
    for child in soup.findAll('url'):
        for grandchild in child.findAll('loc'):
            if grandchild.text[20:29] == 'en/search':
                urls.add(grandchild.text)
    return urls


def get_item_urls(page_url):
    soup = get_soup(page_url)
    figures = soup.findAll('figure', attrs={'class': 'figure item-figure d-flex align-items-stretch'})
    item_urls = set()
    for fig in figures:
        item_urls.add(fig.find('a')['href'])
    return item_urls


def get_page_urls(search_url):
    try:
        page = requests.get(search_url)
        search_url = page.url
        soup = get_soup(search_url)
        pages_links = soup.findAll('a', attrs={'class': 'page-link'})
        page_num = int(pages_links[-2].text)
        page_urls = set()
        for page in range(1, page_num + 1):
            page_urls.add(search_url + '?page=' + str(page))
        return page_urls
    except:
        pass


def write_in_file(item_urls):
    with open('item_urls.txt', 'w+') as f:
        for url in item_urls:
            print(url)
            f.write(f"{url}\n")


from tqdm import tqdm
def get_all_urls(url):
    search_urls = get_search_urls(get_soup(url))
    all_item_urls = set()
    for search in tqdm(search_urls):
        try:
            page_urls = get_page_urls(search)
            for page in  tqdm(page_urls):
                all_item_urls = all_item_urls.union(get_item_urls(page))
        except:
            pass
    return all_item_urls


def get_urls(url, pagenum, main_tag, keyword, sign, class_):
    pages = []
    for i in range(1, pagenum):
        pages.append(f"{url}{sign}page={i}")
    for i in pages:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('div', attrs={'class': f'{main_tag}'})
        for link in soup.find_all('a',
                                  attrs={'href': re.compile(keyword), 'class': class_}):
            with open('urls.txt', 'a') as f:
                f.write(link.get('href'))
                f.write('\n')


def get_pages(mainpage, pagenum, main_tag, keyword, sign, class_):
    pages = []
    for i in range(1, pagenum):
        pages.append(f"{mainpage}{sign}page={i}")
    for i in pages:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('div', attrs={'class': f'{main_tag}'})
        for link in soup.find_all('a',
                                  attrs={'href': re.compile(keyword), 'class': class_}):
            with open('urls.txt', 'a') as f:
                f.write(link.get('href'))
                f.write('\n')
