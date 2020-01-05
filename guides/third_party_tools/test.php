<?php

// Construct a DSN connection string
$dsn = "odbc:Driver={SqreamODBCDriver};Server=<server address>;Port=<server port>;Database=<database name>;User=<username>;Password=<password>;Service=sqream";

// Create a connection
$conn = odbc_connect($dsn,'','',);

if (!($conn)) { 
  echo "Connection to SQream DB via ODBC failed: " . odbc_errormsg ($conn );
}

$sql = "SELECT show_version()";

// Execute the query
$rs = odbc_exec($conn,$sql);

while ($row = odbc_fetch_object($rs)) 
{
    echo ($row);
}

// Finally, close the connection
odbc_close($conn);

?>