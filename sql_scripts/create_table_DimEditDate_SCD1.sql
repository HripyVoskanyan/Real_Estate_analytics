-- Script to create DimEditDate
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    EditDateID_SK STRING,
    EditDate DATE,
    EditDay FLOAT64,
    EditQuarter FLOAT64,
    EditMonth FLOAT64,
    EditYear FLOAT64,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(EditDateID_SK) NOT ENFORCED);

