.. _spark:

*************************
Using Spark With SQream
*************************


Spark may be used for large-scale data processing.


.. contents::
   :local:
   :depth: 1

Installation and Configuration
------------------------------


Before You Begin
~~~~~~~~~~~~~~~~

To use Spark with SQream, it is essential that you have the following installed:

* JDBC version 4.5.6 or later
* SQream version 2022.1.8 or later
* Spark version 3.3.1 or later
* Spark Connector 1.0.0


JDBC
~~~~

If JDBC is not yet configured, follow the :ref:`JDBC Client Drivers page<java_jdbc>` for guidance in registring and configuring.


Connecting Spark to SQream
~~~~~~~~~~~~~~~~~~~

The Spark Connector enables inserting Spark DataFrames into SQream tables and exporting tables or queries as Spark DataFrames for compatibility with Spark. DataFrames are data structures within the Spark framework designed for transferring data between disparate data sources.

1. In the Spark Shell, run:

.. code-block:: postgres

		./spark-shell --driver-class-path {driver path}  --jars {Spark-Sqream-Connector.jar path}


Example:

.. code-block:: postgres

		./spark-shell --driver-class-path /home/sqream/sqream-jdbc-4.5.6.jar  --jars Spark-Sqream-Connector-1.0.jar


Connector Configuration
~~~~~~~~~~~~~~~~~~~~~~~

The Spark JDBC connection properties allow users to configure connections between Spark and databases. These properties enable database access, query execution, and result retrieval, as well as authentication, encryption, and connection pooling.

SQream supports the following Spark connection properties: 

.. list-table:: 
   :widths: 1 4 20
   :header-rows: 1
   
   
   * - Item
     - Default
     - Description
   * - ``url``
     -
     - The JDBC URL to connect to the database.
   * - ``dbtable``
     - 
     - The name of the table or view to be queried or written to in a relational database when using the JDBC data source.
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
     - The default cascading truncate behavior of the JDBC database in question, specified in the ``isCascadeTruncate`` in each JDBCDialect.
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
   * - ``c``
     - ``false``
     - A shorthand for specifying connection properties in the JDBC data source.
   * - ``connectionProvider``
     -
     - A fully qualified class name of a custom connection provider to use when connecting to a data source.
	 

Transferring Data From SQream to Spark
-------------------------------------

#. From the ``SqlContext`` object, use the ``read()`` method to construct a ``DataFrameReader``.

#. Use the ``format()`` method to specify ``SQREAM_SOURCE_NAME``.

#. Use either the ``option()`` or ``options()` method to specify the connector options.

#. Specify one of the following options for reading tables:

 * ``dbtable``: equivalent to the ``SELECT * FROM <table_name>`` command.

 * ``query``: equivalent to the ``SELECT`` statement.
	
Examples
~~~~~~~~

Reading an entire table:

.. code-block:: postgres

	val df: DataFrame = sqlContext.read .format(SQREAM_SOURCE_NAME) .options(sfOptions) .option("<sqream_table_name>", "<table_name>") .load()

Reading query results:
	
.. code-block:: postgres	

	val df: DataFrame = sqlContext.read .format(SQREAM_SOURCE_NAME) .options(sfOptions) .option("query", "<EXECUTED_QUERY> <table_name>") .load()

	
Transferring data From Spark to SQream
--------------------------------------

#. Use the ``write()`` method of the ``DataFrame`` to construct a ``DataFrameWriter``.

#. Specify ``SQREAM_SOURCE_NAME`` using the ``format()`` method.

#. Use either the ``option()`` or the ``options()` method to specify the connector options.

#. To specify the table to which data is written, use the ``dbtable`` option.

#. To specify the content saving mode, use the ``mode()`` method.

Example
~~~~~~~~
Read an entire table:

.. code-block:: postgres

	df.write .format(SQREAM_SOURCE_NAME) .options(sfOptions) .option("<sqream_table_name>", "<table_name>") .mode(SaveMode.Overwrite) .save()


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

		}
	}
	  
