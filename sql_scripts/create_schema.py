# Import necessary modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Create a schema
query = "CREATE SCHEMA Apartments;"

# Execute the SQL query and retrieve the query job
query_job = client.query(query)
