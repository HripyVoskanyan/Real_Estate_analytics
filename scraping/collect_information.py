import requests
from bs4 import BeautifulSoup
import os
import logging
from config import log_folder
from logger_scraping import *


def create_soup(url, config):
    """
    Create a BeautifulSoup object from the HTML content of a web page.

    Parameters:
        url (str): The URL of the web page to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        results (ResultSet): A ResultSet object containing the HTML elements that match the configuration
        specified in the 'config' dictionary.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(config['main'][0], attrs={'class': config['main'][1]})
    logging.info(f"Soup object created of {url}")
    return results


def collect_address(results, config):
    """
    Extracts the address information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The address information extracted from the HTML content, or None if no address was found.
    """
    for row in results:
        try:
            temp = row.find(config['address'][0], attrs={'class': config['address'][1]}).text.replace('\n', "")
            logging.info("Address is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_sqm(results, config):
    """
    Extracts the sqm information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The sqm information extracted from the HTML content, or None if no sqm was found.
    """
    for row in results:
        try:
            temp = row.find(config['sqm'][0], attrs={
                'class': config['sqm'][1]}).text.replace('\n', "")
            logging.info("Sqm is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
    return None


def collect_sqm1(results, config):
    """
    Extracts the sqm information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The sqm information extracted from the HTML content, or None if no sqm was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['sqm'][0], attrs={
                'class': config['sqm'][1]})[config['sqm'][2]].text.replace('\n', "")
            logging.info("Sqm is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_rooms(results, config):
    """
    Extracts the number of rooms information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The number of rooms information extracted from the HTML content, or None if no information was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['rooms'][0], attrs={
                'class': config['rooms'][1]})[config['rooms'][2]].text.replace('\n', "")
            logging.info("Room number is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_floor(results, config):
    """
    Extracts the floor information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The floor information extracted from the HTML content, or None if no floor was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['floor'][0], attrs={
                'class': config['floor'][1]})[config['floor'][2]].text.replace('\n', "").replace(' ', '')
            logging.info("Floor is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_info(results, config):
    """
    Extracts the description information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The description information extracted from the HTML content, or None if no description was found.
    """
    for row in results:
        try:
            temp = row.find(config['info'][0], attrs={
                'class': config['info'][1]}).text.replace('\n', "")
            logging.info("Description is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_price(results, config):
    """
    Extracts the price information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The price information extracted from the HTML content, or None if no price was found.
    """
    for row in results:
        try:
            temp = row.find(config['price'][0], attrs={
                'class': config['price'][1]}).text.replace('\n', "")
            logging.info("Price is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_more(results, config):
    """
    Extracts more information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: More information extracted from the HTML content, or None if no information was found.
    """
    for row in results:
        try:
            temp = row.find(config['more'][0], attrs={
                'class': config['more'][1]}).text.replace('\n', "")
            logging.info("More information is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_views(results, config):
    """
    Extracts the number of views information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The number of views information extracted from the HTML content, or None if no views was found.
    """
    for row in results:
        try:
            temp = row.find(config['views'][0], attrs={
                'class': config['views'][1]}).text
            logging.info("View number is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_data_lat(results, config):
    """
    Extracts the latitude information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The latitude information extracted from the HTML content, or None if no latitude was found.
    """
    for row in results:
        try:
            temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lat']
            logging.info("Latitude is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_data_lng(results, config):
    """
    Extracts the longitude information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The longitude information extracted from the HTML content, or None if no longitude was found.
    """
    for row in results:
        try:
            temp = row.find("div", attrs={"id": "yandex_map_item_view"})['data-lng']
            logging.info("Longitude is collected")
            return temp
        except Exception as e:
            logging.exception(f"Error: {e}")
            pass
    return None


def collect_additional(results, config):
    """
    Extracts the additional information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The additional information extracted from the HTML content, or None if no information was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['additional'][0], attrs={
                'class': config['additional'][1]})[1].findAll(config['additional'][2])
            some_string = ""
            for li in temp:
                some_string += (li.get_text() + '--')
            logging.info("Additional information is collected")
            return some_string + '\n'
        except Exception as e:
            logging.error(f"Error: {e}")
            pass
    return None


def collect_additional0(results, config):
    """
    Extracts the additional information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The additional information extracted from the HTML content, or None if no information was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['additional'][0], attrs={
                'class': config['additional'][1]})[0].findAll(config['additional'][2])
            some_string = ""
            for li in temp:
                some_string += (li.get_text() + '--')

            logging.info("Additional information is collected")
            return some_string + '\n'
        except Exception as e:
            logging.error(f"Error: {e}")
            pass
    return None


def collect_facilities(results, config):
    """
    Extracts the facility information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The facility information extracted from the HTML content, or None if no information was found.
    """
    for row in results:
        try:
            temp = row.find(config['facilities'][0], attrs={
                'class': config['facilities'][1]}).findAll(config['facilities'][2])
            some_string = ""
            for li in temp:
                some_string += (li.get_text() + '--')

            logging.info("Additional information is collected")
            return some_string + '\n'
        except Exception as e:
            logging.error(f"Error: {e}")
            pass
    return None


def collect_Adddate(results, config):
    """
    Extracts the added date information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The added date information extracted from the HTML content, or None if no date was found.
    """
    for row in results:
        try:
            temp = row.find(config['adddate'][0], attrs={'class': config['adddate'][1]}).text.replace('\n', "")
            logging.info("Added date is collected")
            return temp
        except Exception as e:
            logging.error(f"Error: {e}")
    return None


def collect_Editdate(results, config):
    """
    Extracts the edited date information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The edited date information extracted from the HTML content, or None if no date was found.
    """
    for row in results:
        try:
            temp = row.findAll(config['editdate'][0], attrs={'class': config['editdate'][1]})[5].text.replace('\n', "")
            logging.info("Edited date is collected")
            return temp
        except Exception as e:
            logging.error(f"Error: {e}")
    return None


def collect_id(results, config):
    """
    Extracts the natural key information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The natural key information extracted from the HTML content, or None if no id was found.
    """
    for row in results:
        try:
            temp = row.find(config['id'][0], attrs={
                'class': config['id'][1]}).text.replace('ID ', "")
            logging.info("Natural key is collected")
            return temp
        except Exception as e:
            logging.error(f"Error: {e}")
    return None


def collect_type(results, config):
    """
    Extracts the type information from a ResultSet object.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        str: The type information extracted from the HTML content, or None if no type was found.
    """
    for row in results:
        try:
            temp = row.find(config['type'][0], attrs={
                'class': config['type'][1]}).text
            logging.info("Type is collected")
            return temp
        except Exception as e:
            logging.error(f"Error: {e}")
    return None


def collect_all(results, df, config):
    """
    Collects all the relevant information from a ResultSet object and appends it to a pandas DataFrame.

    Parameters:
        results (ResultSet): A ResultSet object containing the HTML elements to scrape.
        df (DataFrame): A pandas DataFrame to which the extracted information will be appended.
        config (dict): A dictionary containing configuration information for the scraping process.

    Returns:
        DataFrame: A pandas DataFrame containing the extracted information.
    """
    app = {'address': collect_address(results, config),
           'sqm': collect_sqm(results, config),
           'sqm0': collect_sqm1(results, config),
           'rooms': collect_rooms(results, config),
           'floor': collect_floor(results, config),
           'info': collect_info(results, config),
           'price': collect_price(results, config),
           'more': collect_more(results, config),
           'views': collect_views(results, config),
           'additional': collect_additional(results, config),
           'additional0': collect_additional0(results, config),
           'facilities': collect_facilities(results, config),
           'data-lat': collect_data_lat(results, config),
           'data-lng': collect_data_lng(results, config),
           'adddate': collect_Adddate(results, config),
           'editdate': collect_Editdate(results, config),
           'id': collect_id(results, config),
           'type': collect_type(results, config)}
    df = df.append(app, ignore_index=True)
    logging.info("All information is collected")
    return df

