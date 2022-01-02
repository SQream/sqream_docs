options sastrace='d,d,d,d'
sastraceloc=saslog
nostsuffix
msglevel=i
sql_ip_trace=(note,source)
DEBUG=DBMS_SELECT;
options validvarname=any;
libname sqlib jdbc driver="com.sqream.jdbc.SQDriver"
   classpath="/opt/sqream/sqream-jdbc-4.5.0.jar"
   URL="jdbc:Sqream://192.168.1.176:3108/master;cluster=true"
   user="sqream"
   password="sqream"
   schema="public"
   PRESERVE_TAB_NAMES=YES
   PRESERVE_COL_NAMES=YES;
proc sql;
   title 'nba table';
   select *
   from sqlib.nba;
quit;
data nba;
   set sqlib.nba;
run;