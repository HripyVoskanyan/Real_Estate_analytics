-- Script to create DimAddDate
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    AddDateID_SK STRING,
    AddDate DATE,
    AddDay FLOAT64,
    AddQuarter FLOAT64,
    AddMonth FLOAT64,
    AddYear FLOAT64,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(AddDateID_SK) NOT ENFORCED);

