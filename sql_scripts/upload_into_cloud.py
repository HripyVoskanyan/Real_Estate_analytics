# Import necessary modules
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.cloud import bigquery
import pandas as pd
import pandas_gbq
from config import *

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate and save the credentials in a local file
    gauth.DEFAULT_SETTINGS['client_config_file'] = r'C:/AUA/Capstone/code/sql_scripts/credentials.json'
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

folder_id = '1DsFpWLqpY4JVlwVwtW1G1w5zk5UZDsee'
query = f"'{folder_id}' in parents and trashed = false"
file_list = drive.ListFile({'q': query}).GetList()

if len(file_list) > 0:
    # Sort file list by modified date
    file_list = sorted(file_list, key=lambda x: x['modifiedDate'], reverse=True)

    # Download the latest modified CSV file
    file_id = file_list[0]['id']
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(file['title'])

    # Load the downloaded CSV file into a Pandas dataframe
    df = pd.read_csv(file['title'])
    print(df.head())

    # Set the project ID and dataset name
    client = bigquery.Client(project=project_id)

    # create a new BigQuery table with an inferred schema
    table_ref = client.dataset(dataset_id).table(table_name)

    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.create_disposition = bigquery.CreateDisposition.CREATE_IF_NEEDED
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_EMPTY

    client.load_table_from_dataframe(df, table_ref, job_config=job_config).result()

    # upload the DataFrame to the new BigQuery table
    pandas_gbq.to_gbq(df, f'{project_id}.{dataset_id}.{table_name}', project_id=project_id, if_exists='append')

    # pandas_gbq.to_gbq(df, table_name, project_id=project_id, if_exists='fail')
    print(f"Data uploaded.")
else:
    print("No CSV files found in the specified folder.")
