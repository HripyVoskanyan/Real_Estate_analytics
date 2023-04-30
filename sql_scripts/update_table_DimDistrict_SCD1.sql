-- Script to load data into DimDistrict
MERGE {project_id}.{dataset_id}.{dst_table_name} dst
using (SELECT district,
              CAST(ingestion_date AS DATE) as ingestion_date,
              Max(staging_raw_id) AS staging_raw_id
       FROM   {project_id}.{dataset_id}.{src_table_name}
       WHERE district IS NOT NULL
       GROUP  BY district,
                 CAST(ingestion_date AS DATE)
                 ) src
ON dst.districtname = src.district
WHEN NOT matched THEN
  INSERT (districtid_sk,
          districtname,
          ingestion_date,
          staging_raw_id)
  VALUES(Generate_uuid(),
         src.district,
         src.ingestion_date,
         src.staging_raw_id);