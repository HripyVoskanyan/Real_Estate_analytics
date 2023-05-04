import config
import tasks
import os
import logging
from config import log_folder
from logger_infrastructure import *

if not os.path.exists(log_folder):
    os.makedirs(log_folder)


if __name__ == "__main__":
    client = tasks.create_client(
        cred_json=config.cred_json, project_id=config.project_id
    )
    logging.info(f"Client object has been created in {config.project_id}")

    # creating the schema
    tasks.create_schema(
        client=client, project_id=config.project_id, dataset_id=config.dataset_id
    )
    logging.info(f"Schema {config.dataset_id }has been created in {config.project_id}")

    # dropping tables if they exist
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimDistrict_SCD1",
    )
    logging.info("DimDistrict_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimStreet_SCD1",
    )
    logging.info("DimStreet_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimPlatform_SCD1",
    )
    logging.info("DimPlatform_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimType_SCD1",
    )
    logging.info("DimType_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimHouseType_SCD1",
    )
    logging.info("DimHouseType_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimAddDate_SCD1",
    )
    logging.info("DimAddDate_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimEditDate_SCD1",
    )
    logging.info("DimEditDate_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimRegion_SCD1",
    )
    logging.info("DimRegion_SCD1 has been dropped")
    tasks.drop_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="FactHouse_SCD2",
    )
    logging.info("FactHouse_SCD2 has been dropped")

    # creating tables
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimDistrict_SCD1",
    )
    logging.info("DimDistrict_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimStreet_SCD1",
    )
    logging.info("DimStreet_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimPlatform_SCD1",
    )
    logging.info("DimPlatform_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimType_SCD1",
    )
    logging.info("DimType_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimHouseType_SCD1",
    )
    logging.info("DimHouseType_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimAddDate_SCD1",
    )
    logging.info("DimAddDate_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimEditDate_SCD1",
    )
    logging.info("DimEditDate_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="DimRegion_SCD1",
    )
    logging.info("DimRegion_SCD1 has been created")
    tasks.create_table(
        client=client,
        project_id=config.project_id,
        dataset_id=config.dataset_id,
        table_name="FactHouse_SCD2",
    )
    logging.info("FactHouse_SCD2 has been created")
