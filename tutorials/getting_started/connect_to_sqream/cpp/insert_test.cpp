// Insert with parameterized statement example

#include <iostream>

#include  "sqream.h"

int main () {

   sqream::driver  sqc;

   // Connection parameters: Hostname, Port, Use SSL, Username, Password, Database name, Service name
   sqc.connect("127.0.0.1",  5000,  false,  "rhendricks",  "Tr0ub4dor&3",  "raviga", "sqream");

   std::string statement = "CREATE TABLE animals (id INT NOT NULL, name VARCHAR(10) NOT NULL)";
   run_direct_query(&sqc,  statement);
   
   statement = "INSERT INTO animals VALUES (?, ?)";

   sqc.new_query(statement);
   sqc.execute_query();

   // Sample data set
   int len = 3;
   int row1[len] = {1,2,3};
   std::string row2[len] = {"Dog","Cat","Possum"};

   for (int idx = 0; idx < len; ++idx) {  
      sqc.set_int(0, row1[idx]);
      sqc.set_varchar(1, row2[idx]);

      sqc.next_query_row();
   }  

   sqc.finish_query(); // This commits the data to the table

   sqc.disconnect();

}
