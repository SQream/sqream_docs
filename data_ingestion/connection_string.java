##Postgresql, Oracle, and SQreamDB Connection Strings - mandatory!
	
#postgres
source.jdbc.connectionstring=jdbc:postgresql://<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
#oracle
source.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>&ssl=<true/false>
	
#sqream
sqream.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>
	

##Optional 
	
#Oracle
#catalog.jdbc.connectionstring=jdbc:oracle:thin:@//<HostIp:port>/<database_name>?user=<user_name>&password=<password>

#SQreamDB
#catalog.jdbc.connectionstring=jdbc:Sqream://<HostIp:port>/<database_name>;cluster=<true/false>;user=<user_name>;password=<password>