.. _preparing_oracle_for_data_migration:

***********************************
Preparing Oracle for Data Migration
***********************************

The preparation of incremental and Change Data Capture (CDC) tables is essential for efficiently tracking and managing changes to data over time, enabling streamlined data synchronization, and replication.

Preparing CDC Tables
====================

1. Prepare the data table:

   .. code-block:: sql

	-- Drop the existing table if it exists
	DROP TABLE cdc_example;

	-- Create the main data table
	CREATE TABLE cdc_example (
	    id NUMBER(8) PRIMARY KEY,
	    id_name VARCHAR(8),
	    dttm TIMESTAMP,
	    f_col FLOAT
	);

	-- Insert initial data into the table
	INSERT INTO cdc_example (id, id_name, dttm, f_col) VALUES (-1, 'A', CURRENT_TIMESTAMP, 0);

	-- Verify the data in the table
	SELECT * FROM cdc_example ORDER BY id DESC;


2. Prepare the CDC catalog:

   .. code-block:: sql

	-- Drop the CDC table if it exists
	DROP TABLE cdc_example_cdc;

	-- Create the CDC table to store change data
	CREATE TABLE cdc_example_cdc (
	    id NUMBER(8),
	    id_name VARCHAR(8),
	    row_id ROWID,
	    updated_dttm DATE,
	    type VARCHAR2(1)
	);

	-- Insert record to CDC_TABLES in the catalog
	INSERT INTO public.CDC_TABLES (
	    DB_NAME, 
	    SCHEMA_NAME, 
	    TABLE_NAME, 
	    TABLE_NAME_FULL, 
	    TABLE_NAME_CDC, 
	    INC_COLUMN_NAME, 
	    INC_COLUMN_TYPE, 
	    LOAD_TYPE, 
	    FREQ_TYPE, 
	    FREQ_INTERVAL, 
	    IS_ACTIVE, 
	    STATUS_LOAD, 
	    INC_GAP_VALUE
	) VALUES (
	    'ORCL', 
	    'QA', 
	    'CDC_EXAMPLE', 
	    'QA.CDC_EXAMPLE', 
	    'QA.CDC_EXAMPLE_CDC', 
	    NULL, 
	    NULL, 
	    'CDC', 
	    NULL, 
	    NULL, 
	    1, 
	    0, 
	    0
	);

	-- Insert record to primary keys table in the catalog
	INSERT INTO public.CDC_TABLE_PRIMARY_KEYS (
	    DB_NAME, 
	    SCHEMA_NAME, 
	    TABLE_NAME, 
	    TABLE_NAME_FULL, 
	    CONSTRAINT_NAME, 
	    COLUMN_NAME, 
	    IS_NULLABLE
	) VALUES (
	    'ORCL', 
	    'QA', 
	    'CDC_EXAMPLE', 
	    'QA.CDC_EXAMPLE', 
	    NULL, 
	    'ID', 
	   0
	);


3. Create trigger on data table:

   .. code-block:: sql

	-- Create a trigger on the data table to track changes and populate the CDC table
	CREATE OR REPLACE TRIGGER cdc_example_tracking 
	AFTER UPDATE OR INSERT OR DELETE ON cdc_example 
	FOR EACH ROW 
	DECLARE 
	    l_xtn VARCHAR2(1); 
	    l_id INTEGER; 
	    l_id_name VARCHAR2(1); 
	    r_rowid ROWID; 
	BEGIN 
	    l_xtn := CASE 
	                 WHEN UPDATING THEN 'U' 
	                 WHEN INSERTING THEN 'I' 
	                 WHEN DELETING THEN 'D' 
	             END; 
				 
		l_id_name := CASE 
	                     WHEN UPDATING THEN :NEW.id_name 
	                     WHEN INSERTING THEN :NEW.id_name 
	                     WHEN DELETING THEN :OLD.id_name 
	                 END; 
					 
		l_id := CASE 
	                WHEN UPDATING THEN :NEW.id 
	                WHEN INSERTING THEN :NEW.id 
	                WHEN DELETING THEN :OLD.id 
	            END; 
				
		r_rowid := CASE 
	                   WHEN UPDATING THEN :NEW.rowid 
	                   WHEN INSERTING THEN :NEW.rowid 
	                   WHEN DELETING THEN :OLD.rowid 
	               END; 
				   
		INSERT INTO cdc_example_cdc (
	        id, 
	        id_name, 
	        row_id, 
	        updated_dttm, 
	        type
		) VALUES (
	        l_id, 
	        l_id_name, 
	        r_rowid, 
	        SYSDATE, 
	        l_xtn
	   ); 
	END;

Preparing Incremental Table
===========================

1. Prepare the data table:

   .. code-block:: sql

	-- Create the data table for incremental loading
	CREATE TABLE inc_example (
	    ID INT PRIMARY KEY,
	    name VARCHAR(8)
	);

	-- Insert initial data into the table
	INSERT INTO inc_example (ID, name) VALUES (1, 'A');

	-- Verify the data in the table
	SELECT * FROM inc_example;
	
2. Prepare the CDC catalog:

.. code-block:: sql

	-- Insert record into CDC_TABLES in the catalog
	INSERT INTO public.CDC_TABLES (
	    DB_NAME, 
	    SCHEMA_NAME, 
	    TABLE_NAME, 
	    TABLE_NAME_FULL, 
	    INC_COLUMN_NAME, 
	    INC_COLUMN_TYPE, 
	    LOAD_TYPE, 
	    IS_ACTIVE, 
	    STATUS_LOAD
	) VALUES (
	    'ORCL', 
	    'QA', 
	    'INC_EXAMPLE', 
	    'QA.INC_EXAMPLE', 
	    'ID', 
	    'INT', 
	    'INC', 
	    1, 
	    0
	);

	-- Insert record into primary keys table in the catalog
	INSERT INTO public.CDC_TABLE_PRIMARY_KEYS (
	    DB_NAME, 
	    SCHEMA_NAME, 
	    TABLE_NAME, 
	    TABLE_NAME_FULL, 
	    COLUMN_NAME, 
	    IS_NULLABLE
	) VALUES (
	    'ORCL', 
	    'QA', 
	    'INC_EXAMPLE', 
	    'QA.INC_EXAMPLE', 
	    'ID', 
	    0
	);

