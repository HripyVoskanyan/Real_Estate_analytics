-- Script to load data into DimDistrict
MERGE {project_id}.{dataset_id}.{dst_table_name} dst using (
  SELECT
    housetype,
    CAST(ingestion_date AS DATE) as ingestion_date,
    Max(staging_raw_id) AS staging_raw_id
  FROM
    {project_id}.{dataset_id}.{src_table_name}
  WHERE
    housetype IS NOT NULL
    AND ingestion_date = '{ingestion_date}'
  GROUP BY
    housetype,
    CAST(ingestion_date AS DATE)
) src ON dst.housetypename = src.housetype WHEN NOT matched THEN INSERT (
  housetypeid_sk, housetypename, ingestion_date,
  staging_raw_id
)
VALUES
  (
    Generate_uuid(),
    src.housetype,
    src.ingestion_date,
    src.staging_raw_id
  );
