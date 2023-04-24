from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)
query = "CREATE TABLE IF NOT EXISTS capstone-384712.Apartments.DimAddDate (AddDatekey STRING, Adddate DATE, " \
        "AddDay FLOAT64, AddQuarter FLOAT64, AddMonth FLOAT64, AddYear FLOAT64, PRIMARY KEY(AddDateKey) NOT ENFORCED); "
query_job = client.query(query)
