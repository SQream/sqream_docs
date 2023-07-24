####mandatory!

##Postgresql, Oracle, and SQreamDB Connection Strings
	
#postgres
source.jdbc.connectionstring=jdbc:postgresql://<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
#oracle
source.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
#sqream
sqream.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>
	
##CDC and Incremental Parameter

cdc_catalog_table=SMSDW.CDC_TABLES
cdc_tracking_table=SMSDW.CDC_TRACKING
cdc_primary_keys_table=SMSDW.CDC_TABLE_PRIMARY_KEYS



####Optional!
	
#Oracle Catalog
#catalog.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>

#SQreamDB Catalog
#catalog.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>

#Summary Parameter
#load_summary_table=SMSDW.SQLOAD_SUMMARY