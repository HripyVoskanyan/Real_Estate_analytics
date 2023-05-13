import config
import tasks

if __name__ == "__main__":
    client = tasks.create_client(
        cred_json=config.cred_json, project_id=config.project_id
    )

    # check the data in the tables
    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimAddDate_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimDistrict_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimEditDate_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimHouseType_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimPlatform_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimRegion_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimStreet_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="DimType_SCD1")

    tasks.check_data(client=client, project_id=config.project_id,
                     dataset_id=config.dataset_id, table_name="FactHouse_SCD2")
