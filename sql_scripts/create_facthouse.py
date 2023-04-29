# Import necessary modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

# Authenticate and create a BigQuery client
credentials = service_account.Credentials.from_service_account_file(cred_json)
client = bigquery.Client(credentials=credentials, project=project_id)

# Create a new table if it doesn't already exist
query = "CREATE TABLE IF NOT EXISTS capstone-384712.Apartments.FactHouse (ListingID STRING, StreetID STRING, " \
        "DistrictID STRING, PlatformID STRING, TypeID STRING, HousetypeID STRING, AddDatekey STRING, EditDatekey " \
        "STRING, sqm  STRING, rooms STRING, floor_ STRING, price  STRING, views FLOAT64,lng FLOAT64, lat FLOAT64, " \
        "eurowindows FLOAT64, irondoor FLOAT64, openbalcony FLOAT64, securitysystem FLOAT64, sunny FLOAT64, " \
        "view_ FLOAT64, roadside FLOAT64, closetothebusstation FLOAT64, parking FLOAT64, park FLOAT64, " \
        "elevator FLOAT64, furniture FLOAT64, equipment FLOAT64, balcony FLOAT64, storageroom FLOAT64, playground " \
        "FLOAT64, parquet FLOAT64, tile FLOAT64, laminateflooring FLOAT64, heating FLOAT64, hotwater FLOAT64, " \
        "electricity FLOAT64, centralheating FLOAT64,  water FLOAT64, water247 FLOAT64, gas FLOAT64, airconditioning " \
        "FLOAT64, sewerage FLOAT64, logha FLOAT64, garage FLOAT64, internet FLOAT64, FOREIGN KEY(ListingID) " \
        "REFERENCES Apartments.DimListing(ListingID) NOT ENFORCED, FOREIGN KEY(StreetID) REFERENCES " \
        "Apartments.DimStreet(StreetID) NOT ENFORCED, FOREIGN KEY(DistrictID) REFERENCES Apartments.DimDistrict(" \
        "DistrictID)NOT ENFORCED, FOREIGN KEY(PlatformID) REFERENCES Apartments.DimPlatform(PlatformID)NOT ENFORCED, " \
        "FOREIGN KEY(TypeID) REFERENCES Apartments.DimType(TypeID)NOT ENFORCED, FOREIGN KEY(HouseTypeID) REFERENCES " \
        "Apartments.DimHouseType(HouseTypeID)NOT ENFORCED, FOREIGN KEY(AddDatekey) REFERENCES Apartments.DimAddDate(" \
        "AddDatekey)NOT ENFORCED, FOREIGN KEY(EditDateKey) REFERENCES Apartments.DimEditDate(EditDateKey)NOT " \
        "ENFORCED, PRIMARY KEY(ListingID, StreetID, DistrictID, TypeID, HouseTypeID, PlatformID, AddDateKey, " \
        "EditDateKey) NOT ENFORCED); "

# Execute the SQL query and retrieve the query job
query_job = client.query(query)
