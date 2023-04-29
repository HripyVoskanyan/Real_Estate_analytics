"""
Imports required libraries and modules.
Creates GoogleAuth instance to authorize PyDrive instance to upload files to Google Drive.
Then reads a CSV file from a given path and adds the current date as a column to the dataframe: ingestion_date.
Saves the updated dataframe to a new CSV file.
Uploads the new CSV file to a specified Google Drive folder.
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import pandas as pd
from config import *

gauth = GoogleAuth()

# Loads previously saved credentials file if available, otherwise authorizes user and saves new credentials.
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.DEFAULT_SETTINGS['client_config_file'] = r'C:/AUA/Capstone/code/sql_scripts/credentials.json'
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

# Reads a CSV file from a given path and adds the current date as a column to the dataframe.
original_file_path = 'C:/AUA/Capstone/code/data/df_clean_test_rent.csv'
df = pd.read_csv(original_file_path)
today = datetime.today().strftime('%Y-%m-%d')
df['ingestion_date'] = today

# Saves the updated dataframe to a new CSV file.
file_name = f'{today}_staging_data.csv'
file_path = f'C:/AUA/Capstone/code/data/{today}_staging_data.csv'
df.to_csv(file_path, index=False)

# Uploads the new CSV file to a specified Google Drive folder.
file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
file.SetContentFile(file_path)
file.Upload()
