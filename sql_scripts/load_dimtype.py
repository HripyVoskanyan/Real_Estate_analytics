"""
Merge unique type values from staging table into target table
"""

# Import necessary modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import project_id, cred_json

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Construct a SQL query to merge data from staging table to target table
query = "MERGE capstone-384712.Apartments.DimType dt USING (SELECT DISTINCT type FROM " \
        "capstone-384712.Apartments.staging_data) d ON dt.TypeName = d.type WHEN NOT MATCHED THEN INSERT (TypeID, " \
        "TypeName) VALUES(GENERATE_UUID(), d.type); "
query_job = client.query(query)
