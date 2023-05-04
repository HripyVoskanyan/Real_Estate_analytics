import config
import tasks
import os
import argparse
from logger_flow import *


parser = argparse.ArgumentParser(description="My script description")
parser.add_argument(
    "--ingestion_date", type=str, required=True, help="The ingestion date for the data"
)
parser.add_argument(
    "--reload",
    default=None,
    type=bool,
    required=False,
    help="Whether to reload the module",
)
args = parser.parse_args()

if args.ingestion_date:
    print(f"The ingestion date is {args.ingestion_date}")

if __name__ == "__main__":
    client = tasks.create_client(
        cred_json=config.cred_json, project_id=config.project_id
    )
    logging.info(f"Client has been created in {config.project_id}")

    # Upload csv file from local computer to Google Drive folder
    tasks.upload_from_local_to_drive(
        gauth_cred=config.gauth_cred,
        client_config_file=config.client_config_file,
        original_file_path=config.original_file_path,
        folder_id=config.folder_id,
    )
    logging.info(
        f"Data has been uploaded into {config.folder_id} folder of Google Drive"
    )

    if args.reload:
        tasks.delete_from_table(
            client=client,
            project_id=config.project_id,
            dataset_id=config.dataset_id,
            table_name=config.table_name,
            ingestion_date=args.ingestion_date,
        )

    # Upload csv file from Google Drive to Google Cloud project
    tasks.ingest_from_archive_to_staging_raw(
        gauth_cred=config.gauth_cred,
        project_id=config.project_id,
        table_name=config.table_name,
        dataset_id=config.dataset_id,
        folder_id=config.folder_id,
        client_config_file=config.client_config_file,
    )

    logging.info(
        f"Data has been uploaded into Google Cloud {config.folder_id}, {config.dataset_id} dataset with the "
        f"name {config.table_name}."
    )

    # Updating tables in BigQuery
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimDistrict_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimDistrict_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimStreet_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimStreet_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimPlatform_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimPlatform_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimType_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimType_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimHouseType_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimHouseType_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimAddDate_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimAddDate_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimEditDate_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimEditDate_SCD1.")
    tasks.update_dim_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="DimRegion_SCD1",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into DimRegion_SCD1.")
    tasks.update_fact_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        dst_table_name="FactHouse_SCD2",
        src_table_name=config.table_name,
        ingestion_date=args.ingestion_date,
    )
    logging.info(f"Data has been uploaded into FactHouse_SCD2.")
