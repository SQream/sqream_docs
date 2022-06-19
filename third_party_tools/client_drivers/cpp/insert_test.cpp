// Insert with parameterized statement example

#include <iostream>

#include  "sqream.h"

int main () {

   sqream::driver sqc;

   // Connection parameters: Hostname, Port, Use SSL, Username, Password,
   // Database name, Service name
   sqc.connect("127.0.0.1", 5000, false, "rhendricks", "Tr0ub4dor&3",
               "raviga", "sqream");

   run_direct_query(&sqc,
       "CREATE TABLE animals (id INT NOT NULL, name TEXT NOT NULL)");

   // prepare the statement
   sqc.new_query("INSERT INTO animals VALUES (?, ?)");
   sqc.execute_query();

   // Data to insert
   int row0[] = {1,2,3};
   std::string row1[] = {"Dog","Cat","Possum"};
   int len = sizeof(row0)/sizeof(row0[0]);

   for (int i = 0; i < len; ++i) {  
      sqc.set_int(0, row0[i]);
      sqc.set_text(1, row1[i]);
      sqc.next_query_row();
   }  

   // This commits the insert
   sqc.finish_query(); 

   sqc.disconnect();

}
