-- Script to load data into DimEditDate
MERGE {project_id}.{dataset_id}.{dst_table_name} dst using (
  SELECT
    CAST(editdate AS DATE) as editdate,
    edityear,
    editmonth,
    editday,
    editquarter,
    CAST(ingestion_date AS DATE) as ingestion_date,
    Max(staging_raw_id) AS staging_raw_id
  FROM
    {project_id}.{dataset_id}.{src_table_name}
  WHERE
    editdate IS NOT NULL
    AND ingestion_date = '{ingestion_date}'
  GROUP BY
    editdate,
    edityear,
    editmonth,
    editday,
    editquarter,
    CAST(ingestion_date AS DATE)
) src ON dst.editdate = CAST(src.editdate AS DATE) WHEN NOT matched THEN INSERT (
  editdateid_sk, editdate, edityear,
  editmonth, editday, editquarter,
  ingestion_date, staging_raw_id
)
VALUES
  (
    Generate_uuid(),
    src.editdate,
    edityear,
    editmonth,
    editday,
    editquarter,
    src.ingestion_date,
    src.staging_raw_id
  );
