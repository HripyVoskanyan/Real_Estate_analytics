from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)
query = "CREATE TABLE IF NOT EXISTS capstone-384712.Apartments.DimEditDate (EditDatekey STRING, Editdate DATE, " \
        "EditDay FLOAT64, EditQuarter FLOAT64, EditMonth FLOAT64, EditYear FLOAT64, PRIMARY KEY(EditDateKey) NOT " \
        "ENFORCED); "
query_job = client.query(query)
