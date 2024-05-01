import java.sql.Connection;  
import java.sql.DatabaseMetaData;  
import java.sql.DriverManager;  
import java.sql.Statement;  
import java.sql.ResultSet;  

import java.io.IOException;  
import java.security.KeyManagementException;  
import java.security.NoSuchAlgorithmException;  
import java.sql.SQLException;  



public  class  SampleTest  {  

    // Replace with your connection string
    static  final  String  url  =  "jdbc:Sqream://blue_cluster:443/master;accessToken=######################";  

    // Allocate objects for result set and metadata
    Connection  conn    =  null;  
    Statement  stmt  =  null;  
    ResultSet  rs  =  null;  
    DatabaseMetaData  dbmeta  =  null;  

    int  res  =  0;  

    public  void  testJDBC()  throws  SQLException,  IOException  {  

        // Create a connection
        conn  =  DriverManager.getConnection(url);  

        // Create a table with a single integer column
        String sql  =  "CREATE TABLE test (x INT)";
        stmt = conn.createStatement();  // Prepare the statement
        stmt.execute(sql); // Execute the statement
        stmt.close(); // Close the statement handle

        // Insert some values into the newly created table
        sql = "INSERT INTO test VALUES (5),(6)";
        stmt = conn.createStatement();
        stmt.execute(sql);
        stmt.close();

        // Get values from the table
        sql = "SELECT * FROM test";
        stmt = conn.createStatement();
        rs  = stmt.executeQuery(sql);
        // Fetch all results one-by-one
        while(rs.next()) {
            res = rs.getInt(1);
            System.out.println(res); // Print results to screen
        }
        rs.close(); // Close the result set
        stmt.close(); // Close the statement handle
    }


    public  static  void  main(String[]  args)  throws  SQLException,  KeyManagementException,  NoSuchAlgorithmException,  IOException,  ClassNotFoundException{  

        // Load Blue JDBC driver
        Class.forName("com.sqream.jdbc.BlueDriver");  

        // Create test object and run
        SampleTest  test  =  new  SampleTest();  
        test.testJDBC();  
    }  
}