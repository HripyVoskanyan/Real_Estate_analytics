import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import xml.etree.ElementTree as ET


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
    except:
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
            print(url)
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
            for page in  tqdm(page_urls):
                all_item_urls = all_item_urls.union(get_item_urls(page))
        except:
            pass
    return all_item_urls


def get_urls(url, pagenum, main_tag, keyword, sign, class_):
    """
    Extracts URLs from multiple pages of search results based on a specific HTML tag and keyword.

    Parameters:
        url (str): The base URL of the search page.
        pagenum (int): The number of pages of search results to scrape.
        main_tag (str): The name of the HTML tag containing the search results.
        keyword (str): The keyword that the links should contain.
        sign (str): The sign that separates the URL and page number in the pagination links.
        class_ (str): The name of the CSS class that the links should have.

    Returns:
        None

    Writes the extracted URLs to a text file named 'urls.txt' in append mode.
    """
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
    """
    Scrapes pages for links containing a given keyword from a specified main page and writes them to a text file.

    Parameters:
    mainpage (str): The URL of the main page to start scraping from.
    pagenum (int): The number of pages to scrape.
    main_tag (str): The HTML tag containing the link to be scraped.
    keyword (str): The keyword to search for in the link URL.
    sign (str): The character that separates the page number from the URL.
    class_ (str): The CSS class name of the HTML tag containing the link to be scraped.

    Returns:
    None: Writes the scraped links to a text file named 'urls.txt' in the same directory as the script.
    """
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
