"""
Merge unique date values from staging table into target table
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
    "MERGE capstone-384712.Apartments.DimAddDate dl "
    "USING (SELECT DISTINCT PARSE_DATE('%Y-%m-%d', adddate) as adddate, "
    "addyear, addmonth, addday, addquarter "
    "FROM capstone-384712.Apartments.staging_data) d "
    "ON dl.AddDate = d.adddate "
    "WHEN NOT MATCHED THEN INSERT (Adddatekey, AddDate, AddYear, AddMonth, AddDay, AddQuarter) "
    "VALUES(GENERATE_UUID(), d.adddate, d.addyear, d.addmonth, d.addday, d.addquarter); "
)

# Execute the SQL query and retrieve the query job
query_job = client.query(query)

