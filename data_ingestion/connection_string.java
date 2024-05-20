name=connect-jdbc
connectionStringSource=<source database connection string>
connectionStringSqream=<sqreamdb connection string>
connectionStringCatalog=<catalog connection string>

sourceDatabaseName=<source database name>
sourceSchema=<source schema name>
sourceTable=<source table name>

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
cdcCatalogTable=SMSDW.CDC_TABLES
cdcTrackingTable=SMSDW.CDC_TRACKING
loadSummaryTable=SMSDW.SQLOAD_SUMMARY
cdcPrimaryKeyTable=SMSDW.CDC_TABLE_PRIMARY_KEYS
cdcDelete=true
usePartitions=false
lockCheck=false
lockTable=true
loadDttm=false
useDbmsLob=false
