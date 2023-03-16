.. _spark:

*************************
Using Spark With SQream
*************************


The Spark connector enables reading and writing data to and from SQreamDB and may be used for large-scale data processing.


.. contents::
   :local:
   :depth: 1

Installation and Configuration
------------------------------

Before You Begin
~~~~~~~~~~~~~~~~

To use Spark with SQream, it is essential that you have the following installed:

* SQream version 2022.1.8 or later
* Spark version 3.3.1 or later
* SQream Spark Connector 1.0.0
* :ref:`JDBC<jdbc>` version 4.5.6 or later

Connector Configuration
~~~~~~~~~~~~~~~~~~~~~~~

The Spark JDBC connection properties allow users to configure connections between Spark and databases. These properties enable database access, query execution, and result retrieval, as well as authentication, encryption, and connection pooling.

The following Spark connection properties are supported by SQream: 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   
   * - Item
     - Default
     - Description
   * - ``url``
     -
     - The JDBC URL to connect to the database.
   * - ``dbtable``
     - 
     - The JDBC URL to connect to the database.
   * - ``query``
     - 
     - The SQL query to be executed when using the JDBC data source, instead of specifying a table or view name with the dbtable property.
   * - ``driver``
     - 
     - The fully qualified class name of the JDBC driver to use when connecting to a relational database.
   * - ``numPartitions`` 
     - 
     - The number of partitions to use when reading data from a data source.
   * - ``queryTimeout``
     - 0
     - The maximum time in seconds for a JDBC query to execute before timing out.
   * - ``fetchsize``
     - 1
     - The number of rows to fetch in a single JDBC fetch operation.
   * - ``batchsize``
     - 1000000
     - The number of rows to write in a single JDBC batch operation when writing to a database.
   * - ``sessionInitStatement``
     - 
     - A SQL statement to be executed once at the beginning of a JDBC session, such as to set session-level properties.
   * - ``truncate``
     - ``false``
     - A boolean value indicating whether to truncate an existing table before writing data to it.
   * - ``cascadeTruncate``
     - the default cascading truncate behaviour of the JDBC database in question, specified in the ``isCascadeTruncate`` in each JDBCDialect
     - A boolean value indicating whether to recursively truncate child tables when truncating a table.
   * - ``createTableOptions``
     - 
     - Additional options to include when creating a new table in a relational database.
   * - ``createTableColumnTypes``
     - 
     - A map of column names to column data types to use when creating a new table in a relational database.
   * - ``customSchema``
     - 
     - A custom schema to use when reading data from a file format that does not support schema inference, such as CSV or JSON.
   * - ``pushDownPredicate``
     - ``true``
     - A boolean value indicating whether to push down filters to the data source.
   * - ``pushDownAggregate``
     - ``false``
     - A boolean value indicating whether to push down aggregations to the data source.
   * - ``pushDownLimit``
     - ``false``
     - A boolean value indicating whether to push down limits to the data source.
   * - ``pushDownTableSample``
     - ``false``
     - Used to optimize the performance of SQL queries on large tables by pushing down the sampling operation closer to the data source, reducing the amount of data that needs to be processed.
   * - ``connectionProvider``
     -
     - A fully qualified class name of a custom connection provider to use when connecting to a data source.
   * - ``c``
     - ``false``
     - A shorthand for specifying connection properties in the JDBC data source.
	 	


Connecting Spark to SQream
--------------------------

The SQream-Spark Connector enables inserting DataFrames into SQream tables and exporting tables or queries as DataFrames for use with Spark. DataFrames are Spark objects used for transferring data from one data source to another.

1. To open the Spark Shell, run the following command under the ``Spark/bin`` directory:

.. code-block:: postgres

		./spark-shell --driver-class-path {driver path}  --jars {Spark-Sqream-Connector.jar path}


Example:

.. code-block:: postgres

		./spark-shell --driver-class-path /home/sqream/sqream-jdbc-4.5.6.jar  --jars Spark-Sqream-Connector-1.0.jar

2. To create a SQream session, run the following commands in the Spark Shell:

.. code-block:: postgres
	
	import scala.collection.JavaConverters.mapAsJavaMapConverter
	val config = Map("spark.master"->"local").asJava
	import com.sqream.driver.SqreamSession;
	val sqreamSession=SqreamSession.getSession(config)
	

Transferring Data From SQream to Spark
--------------------------------------

1. Create a mapping of Spark options:

.. code-block:: postgres

	val options = Map("query"->"select * from <table_name>", "url"->"jdbc:<jdbc_path>/master;user=<username>;password=<password>;cluster=false").asJava

2. Create a Spark DataFrame:

.. code-block:: postgres

	val df=sqreamSession.read(options)

Transferring Data From Spark to SQream
--------------------------------------

1. Create a mapping of Spark options, using the ``dbtable`` Spark option (``query`` is not allowed for writing): 

.. code-block:: postgres

	val options = Map("dbtable"-> <table_name>", "url"->"jdbc:<jdbc_path>/master;user=<username>;password=<password>;cluster=false").asJava

2. Create a Spark DataFrame:

.. code-block:: postgres

	import org.apache.spark.sql.SaveMode
	val df=sqreamSession.write(df, options, SaveMode.Overwrite)

Supported Data Types and Mapping
--------------------------------

SQream data types mapped to Spark 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - SQream
     - Spark
   * - ``BIGINT``
     - ``LONGINT``
   * - ``BOOL``
     - ``BooleanType``
   * - ``DATE``
     - ``DateType``
   * - ``DOUBLE``
     - ``DoubleType``
   * - ``REAL``
     - ``FloateType``
   * - ``DECIMAL``
     - ``DeciamlType``
   * - ``INT``
     - ``Integer``
   * - ``SMALLINT``
     - ``ShortType``
   * - ``TINYINT``
     - ``ShortType``
   * - ``DATETIME``
     - ``TimestampType``
	 
Spark data types mapped to SQream 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Spark
     - SQream
   * - ``BooleanType``
     - ``BOOL``
   * - ``ByteType``
     - ``SMALLINT``
   * - ``DateType``
     - ``DATE``
   * - ``DecimalType``
     - ``DECIMAL``
   * - ``DoubleType``
     - ``DOUBLE``
   * - ``FloatType``
     - ``REAL``
   * - ``IntegerType``
     - ``INT``
   * - ``LongType``
     - ``BIGINT``
   * - ``ShortType``
     - ``SMALLINT``
   * - ``StringType``
     - ``TEXT``
   * - ``TimestampType``
     - ``DATETIME``
	 

Example
-------
	  
JAVA

.. code-block:: postgres

	import com.sqream.driver.SqreamSession;
	import org.apache.spark.sql.Dataset;
	import org.apache.spark.sql.Row;
	import org.apache.spark.sql.SaveMode;

	import java.util.HashMap;

	public class main {
		public static void main(String[] args) {
			HashMap<String, String> config = new HashMap<>();
			//spark configuration
			//optional configuration here: https://spark.apache.org/docs/latest/configuration.html
			config.put("spark.master", "local");
			SqreamSession sqreamSession = SqreamSession.getSession(config);

			//spark properties
			//optional properties here: https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html
			HashMap<String, String> props = new HashMap<>();

			props.put("url", "jdbc:Sqream://192.168.4.51:5000/master;user=sqream;password=sqream;cluster=false;logfile=logsFiles.txt;loggerlevel=DEBUG");
			props.put("dbtable", "test");

			/*Read from sqream table*/
			Dataset<Row> dataFrame = sqreamSession.read(props);

			/*Added to sqream table*/
			sqreamSession.write(dataFrame, props);
			sqreamSession.write(dataFrame, props, SaveMode.Overwrite);
			

		}
	}
	  
