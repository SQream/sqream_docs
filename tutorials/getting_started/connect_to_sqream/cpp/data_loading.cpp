// This example will examine inserting values from arrays over the network

#include <iostream>

// Import SQream DB header
#include  "sqream.h"

using namespace std;

int main () {

   sqream::driver  sqc; // Create connection object

   // Connection parameters: Hostname, Port, Use SSL, Username, Password, Database name, Service name
   sqc.connect("127.0.0.1",  5000,  false,  "rhendricks",  "Tr0ub4dor&3",  "raviga", "sqream"); // Returns `true` if successfully connected



   // We will create a sample dataset of 3 rows
   int len = 3;

   // Populate values
   int row1[len] = {1,2,3};
   string row2[len] = {"Dog","Cat","Possum"};

   // Create a table
   string statement = "CREATE TABLE cool_animals (id INT NOT NULL, name VARCHAR(10) NOT NULL)";
   run_direct_query(&sqc,  statement); // Prepare and execute in one function

   // Each placeholder symbol (`?`) represents a value we will have to fill
   // Remember to include a placeholder for each column in the table
   statement = "INSERT INTO cool_animals VALUES (?, ?)";

   sqc.new_query(statement); // Prepare statement
   sqc.execute_query(); // Execute statement

   // Fill data
   for (int  idx  =  0;  idx  <  len;  idx  ++)  {  
      sqc.set_int(0,  row1[idx]);        // put a value at column 0 of the table  
      sqc.set_varchar(1,  row2[idx]);    // put a value at column 1 of the table  

      sqc.next_query_row(); // Row is complete, advance to the next row
      // Iterate until no more data to load
   }  

   sqc.finish_query(); // Close the statement handle. This commits the data to the table

   // We're done, so close the connection completely
   sqc.disconnect();


}