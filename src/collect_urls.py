import requests
from bs4 import BeautifulSoup
import re


def get_pages(mainpage, pagenum, main_tag, keyword, sign, class_):
    pages = []
    for i in range(2, pagenum):
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




