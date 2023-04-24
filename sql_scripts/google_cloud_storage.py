from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import pandas as pd

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate and save the credentials in a local file
    gauth.DEFAULT_SETTINGS['client_config_file'] = r'C:/AUA/Capstone/code/sql_scripts/credentials.json'
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

original_file_path = 'C:/AUA/Capstone/code/data/df_clean_test_rent.csv'

df = pd.read_csv(original_file_path)
today = datetime.today().strftime('%Y-%m-%d')
df['ingestion_date'] = today

file_name = f'{today}_staging_data.csv'
file_path = f'C:/AUA/Capstone/code/data/{today}_staging_data.csv'
df.to_csv(file_path, index=False)

folder_id = '1DsFpWLqpY4JVlwVwtW1G1w5zk5UZDsee'

file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
file.SetContentFile(file_path)
file.Upload()
