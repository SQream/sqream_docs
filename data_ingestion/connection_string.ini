# Postgresql, Oracle, Teradata, SAP HANA, Microsoft SQL Server, Sybase and SQreamDB Connection Strings
# (only one source connection string should be specified)

# postgres (and also Greenplum)
connectionStringSource=jdbc:postgresql://<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>

# oracle
connectionStringSource=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>

# teradata
connectionStringSource=jdbc:teradata://<HostIp>/DATABASE=<database_name>,DBS_PORT=<port>,user=<user_name>,password=<password>

# sap hana
connectionStringSource=jdbc:sap://<HostIp>:<port>/?user=<user_name>&password=<password>

# microsoft sql server
connectionStringSource=jdbc:sqlserver://<HostIp>:<port>;databaseName=<database_name>;user=<user_name>;password=<password>;encrypt=<true/false>;trustServerCertificate=<true/false>

# sybase
connectionStringSource=jdbc:sybase:Tds:<HostIp>:<port>/<database_name>?user=<user_name>&password=<password>

# sqream
connectionStringSqream=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>



# Catalog Database Parameters

# Connection string (only one catalog connection string should be specified)
# Catalog database connection string on Oracle:
connectionStringCatalog=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>

# Catalog database connection string on SQreamDB:
connectionStringCatalog=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>



# CDC and Incremental Parameters
cdcCatalogTable=public.CDC_TABLES
cdcTrackingTable=public.CDC_TRACKING
cdcPrimaryKeyTable=public.CDC_TABLE_PRIMARY_KEYS

# Summary table
loadSummaryTable=public.SQLOAD_SUMMARY



# OPTIONAL - Data transfer options
filter=1=1
count=true
limit=2000
threadCount=1
rowid=false
batchSize=500
fetchSize=100000
chunkSize=0
caseSensitive=false
truncate=true
drop=true
loadTypeName=full
cdcDelete=true
usePartitions=false
lockCheck=false
lockTable=true
loadDttm=false
useDbmsLob=false

.. more flags