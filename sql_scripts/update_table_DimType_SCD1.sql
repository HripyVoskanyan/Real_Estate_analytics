-- Script to load data into DimType
MERGE {project_id}.{dataset_id}.{dst_table_name} dst USING (
  SELECT
    type,
    CAST(ingestion_date AS DATE) AS ingestion_date,
    Max(staging_raw_id) AS staging_raw_id
  FROM
    {project_id}.{dataset_id}.{src_table_name}
  WHERE
    type IS NOT NULL
    AND ingestion_date = '{ingestion_date}'
  GROUP BY
    type,
    CAST(ingestion_date AS DATE)
) src ON dst.typename = src.type WHEN NOT MATCHED THEN INSERT (
  typeid_sk, typename, ingestion_date,
  staging_raw_id
)
VALUES
  (
    Generate_uuid(),
    src.type,
    src.ingestion_date,
    src.staging_raw_id
  );
