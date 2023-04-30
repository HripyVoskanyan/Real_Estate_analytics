-- Script to load data into DimRegion
MERGE {project_id}.{dataset_id}.{dst_table_name} dst
using (SELECT city,
              CAST(ingestion_date AS DATE) as ingestion_date,
              Max(staging_raw_id) AS staging_raw_id
       FROM   {project_id}.{dataset_id}.{src_table_name}
       WHERE city IS NOT NULL
       GROUP  BY city,
                 CAST(ingestion_date AS DATE)
                 ) src
ON dst.regionname = src.city
WHEN NOT matched THEN
  INSERT (regionid_sk,
          regionname,
          ingestion_date,
          staging_raw_id)
  VALUES(Generate_uuid(),
         src.city,
         src.ingestion_date,
         src.staging_raw_id);