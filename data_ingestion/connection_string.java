// mandatory!

// Postgresql, Oracle, Teradata, SAP HANA, Microsoft SQL Server, and SQreamDB Connection Strings
	
// postgres
source.jdbc.connectionstring=jdbc:postgresql://<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
// oracle
source.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
// teradata
source.jdbc.connectionstring=jdbc:teradata://<HostIp>/DATABASE=<database_name>,DBS_PORT=<port>,user=<user_name>,password=<password>

// sap hana
source.jdbc.connectionstring=jdbc:sap://<HostIp>:<port>/?user=<user_name>&password=<password>

// microsoft sql server
source.jdbc.connectionstring=jdbc:sqlserver://<HostIp>:<port>;databaseName=<database_name>;user=<user_name>;password=<password>;encrypt=<true/false>;trustServerCertificate=<true/false>	
	
// sqream
sqream.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>
	
// CDC and Incremental Parameter

cdc_catalog_table=public.CDC_TABLES
cdc_tracking_table=public.CDC_TRACKING
cdc_primary_keys_table=public.CDC_TABLE_PRIMARY_KEYS



// Optional!
	
// Oracle Catalog
// catalog.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>

// SQreamDB Catalog
// catalog.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>

// Summary Parameter
// load_summary_table=public.SQLOAD_SUMMARY