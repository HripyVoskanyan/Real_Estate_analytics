"""
Script to clean and preprocess data from MyRealty.am website.

Inputs:
- df_test.csv: CSV file containing the raw data to be cleaned.

Outputs:
- df_clean_test_rent.csv: CSV file containing the cleaned and preprocessed data.

Modules required:
- pandas
- assets.config (configuration file)
- create_dummies (module to create dummy variables)

Notes:
- The script drops the 'Unnamed: 0' column if it exists in the input data.
- The script converts the 'address' column to the 'City', 'District', and 'Street' columns.
- The script creates new columns from the 'sqm' column, including 'Sqm', 'rooms', and 'floor'.
- The script extracts date information from the 'adddate' and 'editdate' columns, including 'addyear', 'edityear',
  'addmonth', 'editmonth', 'addday', 'editday', 'addquarter', and 'editquarter'.
- The script adds the 'platform' column with a platform name.
- The script adds the 'housetype' and 'type' columns based on the values in the 'info' column.
- The script creates dummy variables from the 'additional' column based on the information in the 'info_dict' dictionary.
- The script drops the 'more', 'additional', 'facilities', and 'additional0' columns.
- The script renames the 'data-lat', 'data-lng', and 'id' columns to 'Lat', 'Lng', and 'ListingID_NK', respectively.
"""

import pandas as pd
from assets.config import *
from create_dummies import *
from datetime import datetime
from config import log_folder
import logging
import os
from logger_preprocessing import *


def preprocess_myrealty(df):
    logging.info("Starting data preprocessing...")
    try:
        df = df.drop(["Unnamed: 0"], axis=1)
    except Exception as e:
        logging.exception(f"Error dropping column: {e}")
        pass

    df["address"].replace("", np.nan, inplace=True)
    df.dropna(subset=["address"], inplace=True)
    df["sqm"] = df["sqm"].astype(str)
    df[["Sqm", "sqm"]] = df.sqm.str.split("SQ. M.Room", expand=True)
    df[["rooms", "floor"]] = df.sqm.str.split("Floor/Storeys", expand=True)
    df["Sqm"] = df["Sqm"].str.replace("Area", "")
    df.sqm = df.sqm.str.replace("SQ. M.", "")
    df = df.drop(["sqm"], axis=1)
    df = df.drop(["sqm0"], axis=1)
    df.rooms = df.rooms.astype(str)
    df.rooms = df.rooms.str[:2]
    df.rooms = df.rooms.str.replace("No", "nan")
    df[["price", "pricebysqm"]] = df.price.str.split("/", expand=True)
    df.additional = df.additional.str.replace("\n", "")
    df.facilities = df.facilities.str.replace("\n", "")
    df.adddate = df.adddate.str.slice(start=-12).replace(" ", "")
    df.editdate = df.editdate.str.slice(start=-12).replace(" ", "")
    df.adddate = df.adddate.str.replace("FOR SALE", "")
    df.editdate = df.editdate.str.replace("FOR SALE", "")
    df["addyear"] = pd.DatetimeIndex(df["adddate"]).year
    df["edityear"] = pd.DatetimeIndex(df["editdate"]).year
    df["addmonth"] = pd.DatetimeIndex(df["adddate"]).month
    df["editmonth"] = pd.DatetimeIndex(df["editdate"]).month
    df["addday"] = pd.DatetimeIndex(df["adddate"]).day
    df["editday"] = pd.DatetimeIndex(df["editdate"]).day
    df["addquarter"] = pd.DatetimeIndex(df["adddate"]).quarter
    df["editquarter"] = pd.DatetimeIndex(df["editdate"]).quarter
    df["adddate"] = df["adddate"].str.replace(" ", "")
    df["editdate"] = df["editdate"].str.replace(" ", "")
    df["adddate"] = pd.to_datetime(df["adddate"], format="%d.%m.%Y")
    df["editdate"] = pd.to_datetime(df["editdate"], format="%d.%m.%Y")
    df.price = df.price.str.replace(",", "")
    df["platform"] = "MyRealty.am"
    df["housetype"] = np.where(
        df["info"].str.contains("property"),
        "property",
        np.where(
            df["info"].str.contains("house"),
            "house",
            np.where(df["info"].str.contains("land"), "land", "apartment"),
        ),
    )
    df["type"] = np.where(df["info"].str.contains("rent"), "rent", "sale")
    df[["City", "DistrictStreet"]] = df.address.str.split(",", n=1, expand=True)
    df["DistrictStreet"] = df["DistrictStreet"].str.replace(",", ", ")
    df[["District", "Street"]] = df["DistrictStreet"].str.split(", ", n=1, expand=True)
    df = df.drop(["DistrictStreet"], axis=1)
    df["floor"].replace("", np.nan, inplace=True)
    df["floor"] = df.apply(
        lambda row: row["Sqm"].split("Floor/Storeys ")[-1]
        if "Floor/Storeys" in row["Sqm"]
        else row["floor"],
        axis=1,
    )
    df["Sqm"] = df["Sqm"].str.replace("SQ. M.", "")
    df["Sqm"] = df["Sqm"].str.replace("Floor/Storeys", "")
    df["Sqm"] = df["Sqm"].str.extract("(\d+)")

    create_columns(df)
    create_dummy_columns(df, info_dict, "additional")
    df["pricebysqm"] = df["pricebysqm"].str.replace(" SQ. M. ", "")
    df = df.drop(["more", "additional", "facilities", "additional0"], axis=1)
    df["pricebysqm"] = df["pricebysqm"].str.replace(",", "")
    df["pricebysqm"].replace("", np.nan, inplace=True)
    df["pricebysqm"] = pd.to_numeric(df["pricebysqm"], errors="coerce")
    df = df.rename(columns={"data-lat": "Lat", "data-lng": "Lng", "id": "ListingID_NK"})
    try:
        df = df.drop(["Unnamed: 0"], axis=1)
    except:
        pass
    df.to_csv("C:\AUA\Capstone\code\data\data_new1_clean.csv")
    logging.info("Preprocessing completed successfully.")


def preprocess_besthouse(df):
    logging.info("Starting data preprocessing...")
    try:
        df = df.drop(["Unnamed: 0"], axis=1)
    except Exception as e:
        logging.exception(f"Error dropping column: {e}")
        pass
    df["address"].replace("", np.nan, inplace=True)
    df.dropna(subset=["address"], inplace=True)
    df["sqm0"] = df["sqm0"].str.replace(" m 2", "")
    df = df.rename(columns={"sqm0": "Sqm"})
    df["rooms"] = df["rooms"].str.replace(" ROOM                  ", "")
    df["price"] = df["price"].str.replace("$", "")
    df.price = df.price.str.replace(",", "")
    df.price = df.price.str.replace(" ", "")
    df.id = df.id.str.replace("#", "")
    df[["City", "DistrictStreet"]] = df.address.str.split(",", n=1, expand=True)
    df["DistrictStreet"] = df["DistrictStreet"].str.replace(",", ", ")
    df[["District", "Street"]] = df["DistrictStreet"].str.split(", ", n=1, expand=True)
    df = df.drop(["DistrictStreet", "sqm"], axis=1)

    def convert_date_str(date_str):
        if isinstance(date_str, str):
            try:
                date_obj = datetime.strptime(date_str, "%d-%b")
                date_obj = date_obj.strftime("%m/%d").lstrip("0").replace(" 0", " ")
                return date_obj.replace("/0", "/")
            except ValueError:
                return date_str
        else:
            return np.nan

    df["floor"] = df["floor"].apply(convert_date_str)
    df["platform"] = "BestHouse.am"
    create_columns(df)
    df.additional0 = df.additional0.str.replace(" ", "")
    create_dummy_columns(df, info_dict2, "additional0")

    df = df.drop(["more", "additional", "facilities", "additional0"], axis=1)

    try:
        df = df.drop(["Unnamed: 0"], axis=1)
    except:
        pass
    df.to_csv("C:\AUA\Capstone\code\data\data_new2_clean.csv")
    logging.info("Preprocessing completed successfully.")
