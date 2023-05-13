import pandas as pd
from collect_urls import *
from collect_information import *
import time
import os
from assets.config1 import *
from assets.config2 import *
from config import log_folder
from logger_scraping import *

# Set up logging
if not os.path.exists(log_folder):
    os.makedirs(log_folder)


# all_urls = get_all_urls(sitemap_url)
# write_in_file(all_urls)
df = pd.DataFrame()
with open("item_urls.txt", "r") as f:
    for url0 in f:
        url0 = url0.replace(" ", "")
        url0 = url0.replace("\n", "")
        logging.info(f"Scraping data for URL: {url0}")
        df = collect_all(create_soup(url0, config2), df, config2)
        time.sleep(3)
logging.info("Writing data to CSV")
path = os.path.dirname(os.getcwd()) + '\\' + '\\data\\data_new1.csv'
df.to_csv(path)
