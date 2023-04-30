-- Script to load data into DimAddDate
MERGE {project_id}.{dataset_id}.{dst_table_name} dst
using (SELECT CAST(adddate AS DATE) as adddate,
              addyear,
              addmonth,
              addday,
              addquarter,
              CAST(ingestion_date AS DATE) as ingestion_date,
              Max(staging_raw_id) AS staging_raw_id
       FROM   {project_id}.{dataset_id}.{src_table_name}
       WHERE  adddate IS NOT NULL
       GROUP  BY adddate,
                 addyear,
                 addmonth,
                 addday,
                 addquarter,
                 CAST(ingestion_date AS DATE)) src
ON dst.adddate = CAST(src.adddate AS DATE)
WHEN NOT matched THEN
  INSERT (adddateid_sk,
          adddate,
          addyear,
          addmonth,
          addday,
          addquarter,
          ingestion_date,
          staging_raw_id)
  VALUES(Generate_uuid(),
         src.adddate,
         addyear,
         addmonth,
         addday,
         addquarter,
         src.ingestion_date,
         src.staging_raw_id); 