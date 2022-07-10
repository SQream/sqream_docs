.. _loading_and_unloading_data:

***********************
Loading and Unloading Data
***********************
The **Loading Data** section describes concepts and operations related to importing data into your SQream database:

* `Overview of loading data <https://docs.sqream.com/en/v2020-2/data_ingestion/inserting_data.html>`_ - Describes best practices and considerations for loading data into SQream from a variety of sources and locations.

* `Alternatives to loading data (foreign tables) <https://docs.sqream.com/en/v2020-2/operational_guides/foreign_tables.html>`_ - Useful for running queries directly on external data without importing into your SQream database.

* `Supported data types <https://docs.sqream.com/en/v2020-2/data_type_guides/supported_data_types.html>`_ - Overview of supported data types, including descriptions, examples, and relevant aliases.
   
* `Ingesting data from external sources <https://docs.sqream.com/en/v2020-2/data_ingestion/index.html>`_ - List of data ingestion sources that SQream supports.

* `Inserting data from external tables <https://docs.sqream.com/en/v2020-2/reference/sql/sql_statements/dml_commands/insert.html#insert>`_ - Inserts one or more rows into a table.

* `Ingesting data from third party client platforms <https://docs.sqream.com/en/v2020-2/third_party_tools/client_platforms/index.html>`_ - Gives you direct access to a variety of drivers, connectors, tools, vizualisers, and utilities..

* `Using the COPY FROM statement <https://docs.sqream.com/en/v2020-2/reference/sql/sql_statements/dml_commands/copy_from.html>`_ - Used for loading data from files located on a filesystem into SQream tables. 
   
* `Importing data using Studio <https://docs.sqream.com/en/v2020-2/sqream_studio_5.4.3/executing_statements_and_running_queries_from_the_editor.html#performing-statement-related-operations-from-the-database-tree>`_ - SQream's web-based client providing users with all functionality available from the command line in an intuitive and easy-to-use format.

* `Loading data using Amazon S3 <https://docs.sqream.com/en/v2020-2/operational_guides/s3.html>`_ - Used for loading data from Amazon S3.

* Troubleshooting - Describes troubleshooting solutions related to importing data from the following:

  * `SAS Viya <https://docs.sqream.com/en/v2020-2/troubleshooting/sas_viya_related_issues.html>`_

  * `Tableau <https://docs.sqream.com/en/v2020-2/troubleshooting/tableau_related_issues.html>`_
  
The **Unloading Data** section describes concepts and operations related to exporting data from your SQream database:

* `Overview of unloading data <https://docs.sqream.com/en/v2020-2/operational_guides/external_tables.html>`_ - Describes best practices and considerations for unloading data from SQream to a variety of sources and locations.

* `The COPY TO statement <https://docs.sqream.com/en/v2020-2/reference/sql/sql_statements/dml_commands/copy_to.html>`_ - Used for unloading data from a SQream database table or query to a file on a filesystem.