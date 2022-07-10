options sastrace='d,d,d,d' 
sastraceloc=saslog 
nostsuffix 
msglevel=i 
sql_ip_trace=(note,source) 
DEBUG=DBMS_SELECT;

options validvarname=any;

libname sqlib jdbc driver="com.sqream.jdbc.SQDriver"
   classpath="/opt/sqream/sqream-jdbc-4.0.0.jar" 
   URL="jdbc:Sqream://sqream-cluster.piedpiper.com:3108/raviga;cluster=true" 
   user="rhendricks"
   password="Tr0ub4dor3"
   schema="public" 
   PRESERVE_TAB_NAMES=YES
   PRESERVE_COL_NAMES=YES; 

proc sql;
   title 'Customers table';
   select *
   from sqlib.customers;
quit;

data sqlib.customers;
   set sqlib.customers;