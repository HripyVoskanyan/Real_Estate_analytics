-- Script to load data into DimStreet
MERGE {project_id}.{dataset_id}.{dst_table_name} dst using (
  SELECT
    street,
    CAST(ingestion_date AS DATE) as ingestion_date,
    Max(staging_raw_id) AS staging_raw_id
  FROM
    {project_id}.{dataset_id}.{src_table_name}
  WHERE
    street IS NOT NULL
    AND ingestion_date = '{ingestion_date}'
  GROUP BY
    street,
    CAST(ingestion_date AS DATE)
) src ON dst.streetname = src.street WHEN NOT matched THEN INSERT (
  streetid_sk, streetname, ingestion_date,
  staging_raw_id
)
VALUES
  (
    Generate_uuid(),
    src.street,
    src.ingestion_date,
    src.staging_raw_id
  );
