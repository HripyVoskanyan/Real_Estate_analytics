-- Script to load data into DimPlatform
MERGE {project_id}.{dataset_id}.{dst_table_name} dst using (
  SELECT
    platform,
    CAST(ingestion_date AS DATE) as ingestion_date,
    Max(staging_raw_id) AS staging_raw_id
  FROM
    {project_id}.{dataset_id}.{src_table_name}
  WHERE
    platform IS NOT NULL
    AND ingestion_date = '{ingestion_date}'
  GROUP BY
    platform,
    CAST(ingestion_date AS DATE)
) src ON dst.platformname = src.platform WHEN NOT matched THEN INSERT (
  platformid_sk, platformname, ingestion_date,
  staging_raw_id
)
VALUES
  (
    Generate_uuid(),
    src.platform,
    src.ingestion_date,
    src.staging_raw_id
  );
