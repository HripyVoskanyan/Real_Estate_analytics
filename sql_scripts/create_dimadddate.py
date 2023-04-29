# Import necessary modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Create a new table if it doesn't already exist
query = "CREATE TABLE IF NOT EXISTS capstone-384712.Apartments.DimAddDate (AddDatekey STRING, Adddate DATE, " \
        "AddDay FLOAT64, AddQuarter FLOAT64, AddMonth FLOAT64, AddYear FLOAT64, PRIMARY KEY(AddDateKey) NOT ENFORCED);"

# Execute the SQL query and retrieve the query job
query_job = client.query(query)

