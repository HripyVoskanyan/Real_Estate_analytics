-- Script to create DimDistrict
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    HouseTypeID_SK STRING,
    HouseTypeName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(HouseTypeID_SK) NOT ENFORCED);

