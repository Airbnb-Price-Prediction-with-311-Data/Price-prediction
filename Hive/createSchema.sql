CREATE EXTERNAL TABLE IF NOT EXISTS dataset (
unique_key string,
created_date string,
closed_date string,
agency string,
agency_name string,
complaint_type string,
descriptor string,
location_type string,
incident_zip string,
incident_address string, 
street_name string, 
cross_street_1 string, 
cross_street_2 string, 
intersection_street_1 string, 
intersection_street_2 string, 
address_type string,
city string,
landmark string,                     
facility_type string, 
status string,
date_due string,
resolution_desc string,
date_resolution string,
community_board string,                   
BBL  float ,                             
borough   string,
x_Coordinate float,
y_Coordinate float,
open_data_channel_type string,
park_facility_name   string,
park_borough  string,
vehicle_type  string,
taxi_company_borough string,
taxi_pick_up_location string,
bridge_highway_name string,
bridge_highway_direction string,
road_ramp string,
bridge_highway_segment string,
latitude float,
longitude float,
location string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/amr1215/Data';



