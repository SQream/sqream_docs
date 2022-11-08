import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
​
import java.io.IOException;
import java.sql.SQLException;
​
​
public class SampleTest {
​
   // Replace with your connection string
   private static final String url = "jdbc:Sqream://sqream.mynetwork.co:80/master;user=rhendricks;password=Tr0ub4dor&3";
​
   public void testJDBC() throws SQLException, IOException {
​
       // Create a connection
       try (Connection conn = DriverManager.getConnection(url, "rhendricks", "Tr0ub4dor&3")) {
​
           // Create a table with a single integer column
           try (Statement stmt = conn.createStatement()) {
               stmt.execute("CREATE TABLE test (x INT);");
           }
​
           // Insert some values into the newly created table
           try (Statement stmt = conn.createStatement()) {
               stmt.execute("INSERT INTO test VALUES (5),(6);");
           }
​
           // Get values from the table
           try (Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery("SELECT * FROM test")) {
               int res;
               while (rs.next()) {
                   res = rs.getInt(1);
                   System.out.println(res); // Print results to screen
               }
           }
       }
   }
​
​
   public static void main(String[] args) throws SQLException, IOException, ClassNotFoundException {
​
       // Load SQream DB JDBC driver
       Class.forName("com.sqream.jdbc.BlueDriver");
​
       // Create test object and run
       SampleTest test = new SampleTest();
       test.testJDBC();
   }
}
