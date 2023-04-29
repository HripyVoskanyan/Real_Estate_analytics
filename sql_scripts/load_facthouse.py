# Import required modules
from google.cloud import bigquery
from google.oauth2 import service_account
from config import *

# Load Google Cloud credentials from service account file
credentials = service_account.Credentials.from_service_account_file(cred_json)

# Create BigQuery client object with credentials and project ID
client = bigquery.Client(credentials=credentials, project=project_id)

# Construct a query string to insert data into the FactHouse table
query = "INSERT INTO capstone-384712.Apartments.FactHouse (StreetID, DistrictID, ListingID, PlatformID, TypeID, " \
        "HouseTypeID, sqm, rooms, floor_, price, views, lng, lat, AddDateKey, EditDateKey, eurowindows, irondoor, " \
        "openbalcony, securitysystem, sunny, view_, roadside, closetothebusstation, parking, park, elevator, " \
        "furniture, equipment, balcony, storageroom, playground, parquet, tile, laminateflooring, heating, hotwater, " \
        "electricity, centralheating, water, water247, gas, airconditioning, sewerage, logha, garage, " \
        "internet) SELECT ds.streetid, dd.districtid, dl.listingid, dp.PlatformID, dtt.typeID, dh.Housetypeid, Sqm, " \
        "CAST(rooms AS STRING), floor, price, views, `data-lng`, `data-lat`, dad.AddDateKey, ded.EditDateKey, eurowindows, irondoor, " \
        "openbalcony, securitysystem, sunny, view, roadside, closetothebusstation, parking, park, elevator, " \
        "furniture, equipment, balcony, storageroom, playground, parquet, tile, laminateflooring, heating, hotwater, " \
        "electricity, centralheating, water, water247, gas,  airconditioner, sewerage, logha, garage, internet FROM " \
        "capstone-384712.Apartments.staging_data d LEFT JOIN capstone-384712.Apartments.DimStreet ds on d.street = " \
        "ds.StreetName LEFT JOIN capstone-384712.Apartments.DimDistrict dd on dd.DistrictName = d.district LEFT JOIN " \
        "capstone-384712.Apartments.DimListing dl on dl.Description = d.info LEFT JOIN " \
        "capstone-384712.Apartments.DimPlatform dp on dp.PlatformName = d.platform LEFT JOIN " \
        "capstone-384712.Apartments.DimType dtt on dtt.TypeName = d.type LEFT JOIN " \
        "capstone-384712.Apartments.DimHouseType dh ON dh.Housetype = d.housetype LEFT JOIN " \
        "capstone-384712.Apartments.DimAddDate dad ON dad.AddDate = Date(d.adddate) LEFT JOIN " \
        "capstone-384712.Apartments.DimEditDate ded ON ded.EditDate = Date(d.editdate); "

# Execute the query
query_job = client.query(query)

