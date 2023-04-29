"""
Merge unique date values from staging table into target table
"""

# Import required modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import project_id, cred_json

# Get credentials from service account file and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Build a SQL query to merge staging data with the DimEditDate table
query = "MERGE capstone-384712.Apartments.DimEditDate dl USING (SELECT DISTINCT PARSE_DATE('%Y-%m-%d', editdate) AS " \
        "editdate, edityear, editmonth, editday, editquarter FROM capstone-384712.Apartments.staging_data) d ON " \
        "dl.editdate = d.editdate WHEN NOT MATCHED THEN INSERT (Editdatekey, EditDate, EditYear, EditMonth, EditDay, " \
        "EditQuarter) VALUES (GENERATE_UUID(), d.editdate, d.edityear, d.editmonth, d.editday, d.editquarter); "

# Execute the query using the BigQuery client
query_job = client.query(query)

