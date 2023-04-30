import config
import tasks


if __name__ == '__main__':
    client = tasks.create_client(cred_json=config.cred_json, project_id=config.project_id)

    tasks.upload_from_local_to_drive(gauth_cred=config.gauth_cred, client_config_file=config.client_config_file,
                                     original_file_path=config.original_file_path, folder_id=config.folder_id)

    tasks.upload_from_drive_to_cloud(gauth_cred=config.gauth_cred, project_id=config.project_id,
                                     table_name=config.table_name, dataset_id=config.dataset_id,
                                     folder_id=config.folder_id, client_config_file=config.client_config_file)

    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimDistrict_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimStreet_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimPlatform_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimType_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimHouseType_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimAddDate_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='DimEditDate_SCD1', src_table_name=config.table_name)
    tasks.update_table(client=client, project_id=config.project_id, dataset_id=config.dataset_id,
                       dst_table_name='FactHouse_SCD2', src_table_name=config.table_name)
