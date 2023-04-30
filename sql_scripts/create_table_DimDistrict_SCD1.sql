-- Script to create DimDistrict
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    DistrictID_SK STRING,
    DistrictName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(DistrictID_SK) NOT ENFORCED);

