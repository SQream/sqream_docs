// Import SQream DB headers
#include  "sqream.h"  

sqream::driver  sqc; // Create connection object

// Connection parameters: Hostname, Port, Use SSL, Username, Password, Database name, Service name
sqc.connect("127.0.0.1",  5000,  false,  "rhendricks",  "Tr0ub4dor&3",  "raviga", "sqream");

// The run_direct_query method executes the statement directly

run_direct_query(&sqc,  "CREATE TABLE test (x int)");

run_direct_query(&sqc,  "INSERT INTO test VALUES (5), (6), (7), (8)");

// Now we'll use the prepared statement methods instead to select data from the table

string statement  =  "SELECT * FROM test";

sqc.new_query(statement); // Prepare the statement
sqc.execute_query(); // Execute the statement

// Pull out the data row by row
while  (sqc.next_query_row())
   cout  <<  "Received: "  <<  sqc.get_int(0)  <<  endl; // Print values while there are more rows

sqc.finish_query(); // Close the statement handle when done reading all of the data

// We can now run more statements if we want to

// Close the connection completely
sqc.disconnect();


