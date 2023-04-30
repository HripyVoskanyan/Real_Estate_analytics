-- Script to create DimType
CREATE TABLE IF NOT EXISTS {project_id}.{dataset_id}.{table_name} (
    TypeID_SK STRING,
    TypeName STRING,
    Ingestion_date DATE,
    Staging_Raw_ID STRING,
    PRIMARY KEY(TypeID_SK) NOT ENFORCED);

