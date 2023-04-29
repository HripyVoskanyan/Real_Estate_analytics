"""
Merge unique district values from staging table into target table
"""

# Import necessary modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import project_id, cred_json

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Construct a SQL query to merge data from staging table to target table
query = (
    "MERGE capstone-384712.Apartments.DimDistrict dd "
    "USING (SELECT DISTINCT District FROM "
    "capstone-384712.Apartments.staging_data) d "
    "ON dd.DistrictName = d.District "
    "WHEN NOT MATCHED THEN "
    "INSERT (DistrictID, DistrictName) "
    "VALUES(GENERATE_UUID(), d.District);"
)

# Execute the SQL query and retrieve the query job
query_job = client.query(query)

