-- Script to create DimRegion
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    RegionID_SK STRING,
    RegionName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(RegionID_SK) NOT ENFORCED);

