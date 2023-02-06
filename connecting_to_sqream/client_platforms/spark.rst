.. _spark:

*************************
Using Spark With SQream
*************************


If you are using Spark for distributed processing and analysis and wish to use it with SQream, follow these instructions.


.. contents::
   :local:
   :depth: 1

Installation and Configuration
------------------------------

.. contents::
   :local:
   :depth: 1

Before You Begin
~~~~~~~~~~~~~~~~

To use Spark with SQream, you must have the following installed:

* SQream version 2022.1.8 or later
* Spark version 3.3.1 or later
* SQream Spark Connector 1.0.0
* JDBC version 4.5.6 or later

JDBC
~~~~

If JDBC is not yet configured, follow the `JDBC Client Drivers page <https://docs.sqream.com/en/v2021.1/third_party_tools/client_drivers/jdbc/index.html>`_ for guidance in registring and configuring.


Connecting Spark to SQream
~~~~~~~~~~~~~~~~~~~

The SQream-Spark Connector enables inserting DataFrames into SQream tables and exporting tables or queries as DataFrames for use with Spark. DataFrames are Spark objects used for transferring data from one data source to another.

1. In the Spark Shell, run:

.. code-block:: postgres

		./spark-shell --driver-class-path {driver path}  --jars {Spark-Sqream-Connector.jar path}


Example:

.. code-block:: postgres

		./spark-shell --driver-class-path /home/sqream/sqream-jdbc-4.5.6.jar  --jars Spark-Sqream-Connector-1.0.jar


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
     - The JDBC URL ``jdbc:subprotocol:subname`` establishes the connection between SQream and Spark. Source-specific connection properties may be specified in the URL, such as ``user`` and ``password``, e.g. ``jdbc:Sqream://localhost/test?user=fred&password=secret``.
   * - ``dbtable``
     - 
     - A JDBC table to read from or write to. When reading from a ``dbtable``, anything that is valid in an SQL ``FROM`` clause may be used. For example, you may use a subquery in parentheses instead of querying a full table. It is not allowed to specify ``dbtable`` and ``query`` options at the same time.
   * - ``query``
     - 
     - The ``query`` property in Spark is used to read data into the program by specifying a query. This query is used as a subquery in the ``FROM`` clause and Spark will assign an alias to the subquery. For example, when using a JDBC Source, Spark will issue a query in the format of ``SELECT <columns> FROM (<user_specified_query>) spark_gen_alias``. It's important to note that it is not allowed to use both the ``dbtable`` and ``query`` options at the same time, and the ``query`` option cannot be used with the ``partitionColumn`` option. If the ``partitionColumn`` option is needed, it must be specified using the ``dbtable`` option and qualified using the subquery alias provided in ``dbtable``. An example of how to use this option would be: spark.read.format("jdbc").option("url", jdbcUrl).option("query", "select c1, c2 from t1").load()
   * - ``driver``
     - 
     - The class name of the JDBC driver to use to connect to this URL.
   * - ``numPartitions`` 
     - 
     - The maximum number of partitions that can be used for parallel processing in reading and writing tables. ``numPartitions`` also determines the maximum number of concurrent JDBC connections. If the number of partitions to write exceeds this limit, we decrease it to this limit by calling ``coalesce(numPartitions)`` before writing.
   * - ``queryTimeout``
     - 0
     - The queryTimeout parameter in Spark determines the maximum number of seconds a query can run before it is automatically terminated. Zero means there is no limit. This parameter is used to help ensure that queries do not run for too long and consume excessive resources. The setQueryTimeout() method of the java.sql.Statement interface allows a JDBC driver to specify a timeout for each query instead of an entire JDBC batch. The H2 JDBC driver implements this API and will check the timeout of each query instead of an entire batch.
   * - ``fetchsize``
     - 1
     - The ``fetchsize`` parameter is an integer value that controls the number of rows that are internally fetched by the driver at a time. The ``fetchsize`` parameter can be adjusted to help enhance the performance of JDBC drivers that typically have a low number of rows being fetched (e.g. Oracle with 10 rows).
   * - ``batchsize``
     - 1000000
     - The JDBC batch size, which determines how many rows to insert per round trip. This can help performance on JDBC drivers. This option applies only to writing.
   * - ``sessionInitStatement``
     - 
     - After each database session is opened to the remote DB and before starting to read data, this option executes a custom SQL statement (or a PL/SQL block). Use this to implement session initialization code. Example: ``option("sessionInitStatement", """BEGIN execute immediate 'alter session set "_serial_direct_read"=true'; END;""")``
   * - ``truncate``
     - ``false``
     - This is a JDBC writer related option. When ``SaveMode.Overwrite`` is enabled, this option causes Spark to truncate an existing table instead of dropping and recreating it. This can be more efficient, and prevents the table metadata (e.g., indices) from being removed. However, it will not work in some cases, such as when the new data has a different schema. In case of failures, users should turn off ``truncate`` option to use ``DROP TABLE`` again. Also, due to the different behavior of ``TRUNCATE TABLE`` among DBMS, it's not always safe to use this. MySQLDialect, DB2Dialect, MsSqlServerDialect, DerbyDialect, and OracleDialect supports this while PostgresDialect and default JDBCDirect doesn't. For unknown and unsupported JDBCDirect, the user option ``truncate`` is ignored.
   * - ``cascadeTruncate``
     - the default cascading truncate behaviour of the JDBC database in question, specified in the ``isCascadeTruncate`` in each JDBCDialect
     - This is a JDBC writer related option. If enabled and supported by the JDBC database (PostgreSQL and Oracle at the moment), this options allows execution of a ``TRUNCATE TABLE t CASCADE`` (in the case of PostgreSQL a TRUNCATE TABLE ONLY t CASCADE is executed to prevent inadvertently truncating descendant tables). This will affect other tables, and thus should be used with care.
   * - ``createTableOptions``
     - 
     - This is a JDBC writer related option. If specified, this option allows setting of database-specific table and partition options when creating a table (e.g., ``CREATE TABLE t (name string) ENGINE=InnoDB.``).
   * - ``createTableColumnTypes``
     - 
     - The database column data types to use instead of the defaults, when creating the table. Data type information should be specified in the same format as CREATE TABLE columns syntax (e.g: ``"name CHAR(64), comments VARCHAR(1024)"``). The specified types should be valid spark sql data types.
   * - ``customSchema``
     - 
     - The custom schema to use for reading data from JDBC connectors. For example, ``"id DECIMAL(38, 0), name STRING"``. You can also specify partial fields, and the others use the default type mapping. For example, ``"id DECIMAL(38, 0)"``. The column names should be identical to the corresponding column names of JDBC table. Users can specify the corresponding data types of Spark SQL instead of using the defaults.
   * - ``pushDownPredicate``
     - ``true``
     - The option to enable or disable predicate push-down into the JDBC data source. The default value is true, in which case Spark will push down filters to the JDBC data source as much as possible. Otherwise, if set to false, no filter will be pushed down to the JDBC data source and thus all filters will be handled by Spark. Predicate push-down is usually turned off when the predicate filtering is performed faster by Spark than by the JDBC data source.
   * - ``pushDownAggregate``
     - ``false``
     - The option to enable or disable aggregate push-down in V2 JDBC data source. The default value is false, in which case Spark will not push down aggregates to the JDBC data source. Otherwise, if sets to true, aggregates will be pushed down to the JDBC data source. Aggregate push-down is usually turned off when the aggregate is performed faster by Spark than by the JDBC data source. Please note that aggregates can be pushed down if and only if all the aggregate functions and the related filters can be pushed down. If ``numPartitions`` equals to 1 or the group by key is the same as ``partitionColumn``, Spark will push down aggregate to data source completely and not apply a final aggregate over the data source output. Otherwise, Spark will apply a final aggregate over the data source output.
   * - ``pushDownLimit``
     - ``false``
     - The option to enable or disable LIMIT push-down into V2 JDBC data source. The LIMIT push-down also includes LIMIT + SORT , a.k.a. the Top N operator. The default value is false, in which case Spark does not push down LIMIT or LIMIT with SORT to the JDBC data source. Otherwise, if sets to true, LIMIT or LIMIT with SORT is pushed down to the JDBC data source. If ``numPartitions`` is greater than 1, SPARK still applies LIMIT or LIMIT with SORT on the result from data source even if LIMIT or LIMIT with SORT is pushed down. Otherwise, if LIMIT or LIMIT with SORT is pushed down and ``numPartitions`` equals to 1, SPARK will not apply LIMIT or LIMIT with SORT on the result from data source.
   * - ``pushDownTableSample``
     - ``false``
     - The option to enable or disable TABLESAMPLE push-down into V2 JDBC data source. The default value is false, in which case Spark does not push down TABLESAMPLE to the JDBC data source. Otherwise, if value sets to true, TABLESAMPLE is pushed down to the JDBC data source.
   * - ``connectionProvider``
     -
     - The name of the JDBC connection provider to use to connect to this URL, e.g. ``db2``, ``mssql``. Must be one of the providers loaded with the JDBC data source. Used to disambiguate when more than one provider can handle the specified driver and options. The selected provider must not be disabled by ``spark.sql.sources.disabledJdbcConnProviderList``.
	 

Transferring Data From SQream to Spark
-------------------------------------

In the Spark UI, configure Spark to write to the SQream database.

1. From the SqlContext object, use the read() method to construct a DataFrameReader.

2. Use the format() method to specify SQREAM_SOURCE_NAME.

3. Use either the option() or options() method to specify the connector options.

4. Specify one of the following options for reading tables:

 * dbtable: The name of the table to be read. All columns and records are retrieved (i.e. it is equivalent to ``SELECT * FROM db_table``).

 * query: The exact query (SELECT statement) to run.
	
Examples
---------------

To read an entire table:

.. code-block:: postgres

	val df: DataFrame = sqlContext.read .format(SQREAM_SOURCE_NAME) .options(sfOptions) .option("<sqream_table_name>", "<table_name>") .load()

To read query results:
	
.. code-block:: postgres	

	val df: DataFrame = sqlContext.read .format(SQREAM_SOURCE_NAME) .options(sfOptions) .option("query", "<EXECUTED_QUERY> <table_name>") .load()

	
Transferring data From Spark to SQream
--------------------------------------

In the Spark UI, configure Spark to read from the SQream database.

1. Use the write() method of the DataFrame to construct a DataFrameWriter.

2. Specify SQREAM_SOURCE_NAME using the format() method.

3. Specify the connector options using either the option() or options() method.

4. Use the dbtable option to specify the table to which data is written.

5. Use the mode() method to specify the save mode for the content.

Examples
---------------
To read an entire table:

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
	 

Examples
---------
	  
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
	  
