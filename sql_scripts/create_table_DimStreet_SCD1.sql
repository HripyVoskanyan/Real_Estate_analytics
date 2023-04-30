-- Script to create DimStreet
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    StreetID_SK STRING,
    StreetName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(StreetID_SK) NOT ENFORCED);

