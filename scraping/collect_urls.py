import requests
from bs4 import BeautifulSoup
import re
import os
import logging
from config import log_folder
from tqdm import tqdm
import xml.etree.ElementTree as ET
from logger_scraping import *


def get_soup(url_str):
    """
    Retrieves and parses the HTML content of a webpage using the BeautifulSoup library.

    Parameters:
        url_str (str): The URL of the webpage to retrieve and parse.

    Returns:
        BeautifulSoup: A BeautifulSoup object representing the parsed HTML content of the webpage.
    """
    urlopen = requests.get(url_str).text
    soup = BeautifulSoup(urlopen, 'lxml')
    logging.info(f"Creating soup object of {url_str}")
    return soup


def get_search_urls(soup):
    """
    Extracts the search result URLs from a sitemap XML file.

    Parameters:
        soup (BeautifulSoup): A BeautifulSoup object representing the parsed XML content of the sitemap.

    Returns:
        set: A set of search result URLs extracted from the sitemap.
    """
    urls = set()
    for child in soup.findAll('url'):
        for grandchild in child.findAll('loc'):
            if grandchild.text[20:29] == 'en/search':
                logging.info(f"Finding child URL of {child}")
                urls.add(grandchild.text)
    return urls


def get_item_urls(page_url):
    """
    Extracts the URLs of items listed on a webpage.

    Parameters:
        page_url (str): The URL of the webpage to extract the item URLs from.

    Returns:
        set: A set of URLs of items listed on the webpage.
    """
    soup = get_soup(page_url)
    figures = soup.findAll('figure', attrs={'class': 'figure item-figure d-flex align-items-stretch'})
    item_urls = set()
    for fig in figures:
        item_urls.add(fig.find('a')['href'])
    return item_urls


def get_page_urls(search_url):
    """
    Extracts URLs of all pages of search results from a given search URL.

    Parameters:
        search_url (str): The URL of the search results page.

    Returns:
        set: A set of URLs of all pages of search results.
    """
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
    except Exception as e:
        logging.exception(f"Error getting page urls for {search_url}: {e}")
        pass


def write_in_file(item_urls):
    """
    Writes a set of item URLs to a file named 'item_urls.txt'.

    Parameters:
        item_urls (set): A set of item URLs.

    Returns:
        None
    """
    with open('item_urls.txt', 'w+') as f:
        for url in item_urls:
            logging.info(f"Writing URL to file: {url}")
            f.write(f"{url}\n")


def get_all_urls(url):
    """
    Collects all item URLs from a given URL by iterating through all search pages.

    Parameters:
        url (str): A string representing the starting URL.

    Returns:
        all_item_urls (set): A set of all item URLs.
    """
    search_urls = get_search_urls(get_soup(url))
    all_item_urls = set()
    for search in tqdm(search_urls):
        try:
            page_urls = get_page_urls(search)
            for page in tqdm(page_urls):
                all_item_urls = all_item_urls.union(get_item_urls(page))
        except:
            pass
    return all_item_urls
