-- Script to create DimPlatform
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    PlatformID_SK STRING,
    PlatformName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(PlatformID_SK) NOT ENFORCED);

