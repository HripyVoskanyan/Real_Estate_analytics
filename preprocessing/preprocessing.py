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

df = pd.read_csv("C:\AUA\Capstone\code\data\df_test.csv")

# df = pd.read_excel('C:\AUA\Capstone\code\data\df_rent1.xlsx')
# df2 = pd.read_excel('C:\AUA\Capstone\code\data\df2.xlsx')

try:
    df = df.drop(["Unnamed: 0"], axis=1)
    # df2 = df2.drop(['Unnamed: 0'], axis=1)
except:
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
df['adddate'] = df['adddate'].str.replace(' ', '')
df['editdate'] = df['editdate'].str.replace(' ', '')
df["adddate"] = pd.to_datetime(df["adddate"], format='%d.%m.%Y')
df["editdate"] = pd.to_datetime(df["editdate"], format='%d.%m.%Y')
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
df[["City", "District", "Street"]] = df.address.str.split(",", expand=True)
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

# df2['sqm'] = df2['sqm'].str.replace(' m 2', '')
# df2['rooms'] = df2['rooms'].str.replace(' ROOM                  ', '')
# df2['price'] = df2['price'].str.replace('$ ', '')
# df2['additional0'] = df2['additional0'].str.replace('\n', '')
# df2['facilities'] = df2['facilities'].str.replace('\n', '')


create_columns(df)
# create_columns(df2)
create_dummy_columns(df, info_dict, "additional")
# create_dummy_columns(df2, info_dict2, 'additional0')
df["pricebysqm"] = df["pricebysqm"].str.replace(" SQ. M. ", "")
df = df.drop(["more", "additional", "facilities", "additional0"], axis=1)
df["pricebysqm"] = df["pricebysqm"].str.replace(",", "")
df["pricebysqm"].replace("", np.nan, inplace=True)
df["pricebysqm"] = pd.to_numeric(df["pricebysqm"], errors="coerce")
df = df.rename(columns={"data-lat": "Lat", "data-lng": "Lng", "id": "ListingID_NK"})
# df2 = df2.drop(['additional0', 'facilities'], axis=1)
try:
    df = df.drop(["Unnamed: 0"], axis=1)
#    df2 = df2.drop(['Unnamed: 0'], axis=1)
except:
    pass
df.to_csv("C:\AUA\Capstone\code\data\df_clean_test_rent.csv")
# df2.to_excel('C:\AUA\Capstone\code\data\df2_clean.xlsx')
