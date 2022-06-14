<?php // Construct a DSN connection string
$dsn  = "SqreamODBC"; // Create a connection
$conn = odbc_connect($dsn, '', '');
if (!($conn)) {
    echo "Connection to SQream DB via ODBC failed: " . odbc_errormsg($conn);
}
$sql = "SELECT show_version()"; // Execute the query
$rs  = odbc_exec($conn, $sql);
while (odbc_fetch_row($rs)) {
    for ($i = 1; $i <= odbc_num_fields($rs); $i++) {
        echo "Result is " . odbc_result($rs, $i);
    }
}
echo "\n"; 
odbc_close($conn); // Finally, close the connection
?>
