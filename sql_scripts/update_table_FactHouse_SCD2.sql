-- Script to load data into FactHouse
MERGE {project_id}.{dataset_id}.{dst_table_name} dst USING (
  Select
    Distinct src.ListingID_NK,
    CAST(src.ingestion_date AS DATE) as ingestion_date,
    Max(src.staging_raw_id) AS staging_raw_id,
    ds.StreetID_SK,
    dr.RegionID_SK,
    dd.DistrictID_SK,
    dp.PlatformID_SK,
    dt.TypeID_SK,
    dht.HouseTypeID_SK,
    da.AddDateID_SK,
    de.EditDateID_SK,
    src.SQM,
    CAST(src.rooms AS STRING) As Rooms,
    src.Floor,
    src.Price,
    src.Views,
    src.Lng,
    src.Lat,
    src.EuroWindows,
    src.IronDoor,
    src.OpenBalcony,
    src.SecuritySystem,
    src.Sunny,
    src.view,
    src.RoadSide,
    src.CloseToTheBusStation,
    src.Parking,
    src.Park,
    src.Elevator,
    src.Furniture,
    src.Equipment,
    src.Balcony,
    src.StorageRoom,
    src.Playground,
    src.Parquet,
    src.Tile,
    src.LaminateFlooring,
    src.Heating,
    src.HotWater,
    src.Electricity,
    src.CentralHeating,
    src.Water,
    src.Water247,
    src.Gas,
    src.AirConditioner,
    src.Sewerage,
    src.Logha,
    src.Garage,
    src.Internet
  from
    {project_id}.{dataset_id}.{src_table_name} src
    LEFT JOIN capstone-384712.Apartments.DimPlatform_SCD1 dp ON src.platform = dp.PlatformName
    LEFT JOIN capstone-384712.Apartments.DimRegion_SCD1 dr ON src.city = dr.RegionName
    LEFT JOIN capstone-384712.Apartments.DimStreet_SCD1 ds ON src.street = ds.StreetName
    LEFT JOIN capstone-384712.Apartments.DimDistrict_SCD1 dd ON src.district = dd.DistrictName
    LEFT JOIN capstone-384712.Apartments.DimType_SCD1 dt ON src.type = dt.TypeName
    LEFT JOIN capstone-384712.Apartments.DimHouseType_SCD1 dht ON src.housetype = dht.HouseTypeName
    LEFT JOIN capstone-384712.Apartments.DimAddDate_SCD1 da ON CAST(src.adddate AS DATE) = da.AddDate
    LEFT JOIN capstone-384712.Apartments.DimEditDate_SCD1 de ON CAST(src.editdate AS DATE) = de.EditDate
  WHERE
    src.ingestion_date = '{ingestion_date}'
  GROUP BY
    src.ListingID_NK,
    CAST(src.ingestion_date AS DATE),
    ds.StreetID_SK,
    dr.RegionID_SK,
    dd.DistrictID_SK,
    dp.PlatformID_SK,
    dt.TypeID_SK,
    dht.HouseTypeID_SK,
    da.AddDateID_SK,
    de.EditDateID_SK,
    src.SQM,
    CAST(src.rooms AS STRING),
    src.Floor,
    src.Price,
    src.Views,
    src.Lng,
    src.Lat,
    src.EuroWindows,
    src.IronDoor,
    src.OpenBalcony,
    src.SecuritySystem,
    src.Sunny,
    src.view,
    src.RoadSide,
    src.CloseToTheBusStation,
    src.Parking,
    src.Park,
    src.Elevator,
    src.Furniture,
    src.Equipment,
    src.Balcony,
    src.StorageRoom,
    src.Playground,
    src.Parquet,
    src.Tile,
    src.LaminateFlooring,
    src.Heating,
    src.HotWater,
    src.Electricity,
    src.CentralHeating,
    src.Water,
    src.Water247,
    src.Gas,
    src.AirConditioner,
    src.Sewerage,
    src.Logha,
    src.Garage,
    src.Internet
) src ON dst.ListingID_NK = src.ListingID_NK WHEN NOT MATCHED THEN INSERT (
  ListingID_NK, ingestion_date, Staging_Raw_ID,
  StreetID_SK, RegionID_SK, DistrictID_SK,
  PlatformID_SK, TypeID_SK, HouseTypeID_SK,
  AddDateID_SK, EditDateID_SK, SQM,
  Rooms, Floors, Price, Views, Lng, Lat,
  EuroWindows, IronDoor, OpenBalcony,
  SecuritySystem, Sunny, View_, RoadSide,
  CloseToTheBusStation, Parking, Park,
  Elevator, Furniture, Equipment, Balcony,
  StorageRoom, Playground, Parquet,
  Tile, LaminateFlooring, Heating,
  HotWater, Electricity, CentralHeating,
  Water, Water247, Gas, AirConditioning,
  Sewerage, Logha, Garage, Internet
)
VALUES
  (
    src.ListingID_NK,
    Ingestion_date,
    Staging_Raw_ID,
    src.StreetID_SK,
    src.RegionID_SK,
    src.DistrictID_SK,
    src.PlatformID_SK,
    src.TypeID_SK,
    src.HouseTypeID_SK,
    src.AddDateID_SK,
    src.EditDateID_SK,
    CAST(src.SQM AS STRING),
    CAST(src.rooms AS STRING),
    src.Floor,
    src.Price,
    src.views,
    src.Lng,
    src.Lat,
    src.EuroWindows,
    src.IronDoor,
    src.OpenBalcony,
    src.SecuritySystem,
    src.Sunny,
    src.view,
    src.RoadSide,
    src.CloseToTheBusStation,
    src.Parking,
    src.Park,
    src.Elevator,
    src.Furniture,
    src.Equipment,
    src.Balcony,
    src.StorageRoom,
    src.Playground,
    src.Parquet,
    src.Tile,
    src.LaminateFlooring,
    src.Heating,
    src.HotWater,
    src.Electricity,
    src.CentralHeating,
    src.Water,
    src.Water247,
    src.Gas,
    src.AirConditioner,
    src.Sewerage,
    src.Logha,
    src.Garage,
    src.Internet
  ) WHEN MATCHED
  AND (
    IFNULL(dst.StreetID_SK, '') <> IFNULL(src.StreetID_SK, '')
    OR IFNULL(dst.RegionID_SK, '') <> IFNULL(src.RegionID_SK, '')
    OR IFNULL(dst.DistrictID_SK, '') <> IFNULL(src.DistrictID_SK, '')
    OR IFNULL(dst.PlatformID_SK, '') <> IFNULL(src.PlatformID_SK, '')
    OR IFNULL(dst.TypeID_SK, '') <> IFNULL(src.TypeID_SK, '')
    OR IFNULL(dst.HouseTypeID_SK, '') <> IFNULL(src.HouseTypeID_SK, '')
    OR IFNULL(dst.SQM, '') <> IFNULL(CAST(src.SQM AS STRING), '')
    OR IFNULL(dst.Rooms, '') <> CAST(
      IFNULL(src.rooms, '') AS STRING
    )
    OR IFNULL(dst.Price, '') <> IFNULL(src.Price, '')
    OR IFNULL(dst.Floors, '') <> IFNULL(src.Floor, '')
  ) THEN
UPDATE
SET
  StreetID_SK = src.StreetID_SK,
  RegionID_SK = src.RegionID_SK,
  DistrictID_SK = src.DistrictID_SK,
  PlatformID_SK = src.PlatformID_SK,
  TypeID_SK = src.TypeID_SK,
  HouseTypeID_SK = src.HouseTypeID_SK,
  SQM = CAST(src.SQM AS STRING),
  Rooms = CAST(src.rooms AS STRING),
  Floors = src.Floor,
  Price = src.Price
