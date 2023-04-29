"""
Merge unique house type values from staging table into target table
"""

# Import required modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import project_id, cred_json

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Construct a SQL query to merge data from staging table to target table
query = (
    "MERGE capstone-384712.Apartments.DimHouseType dt "
    "USING (SELECT DISTINCT housetype FROM "
    "capstone-384712.Apartments.staging_data) d "
    "ON dt.Housetype = d.housetype "
    "WHEN NOT MATCHED THEN "
    "INSERT (HouseTypeID, Housetype) "
    "VALUES(GENERATE_UUID(), d.housetype);"
)

# Execute the SQL query and retrieve the query job
query_job = client.query(query)

