.. _seeing_system_objects_as_ddl:

****************************
Seeing System Objects as DDL
****************************

Seeing System Objects as DDL means observing database system objects such as tables or views in terms of the SQL commands (DDL) that were used to create them, offering insights into the database structure.

Dumping Objects
===============

**Tables**

1. Get the table DDL:

   .. code-block:: psql

	SELECT GET_DDL('cool_animals');
	create table "public"."cool_animals" (
	 "id" int not null,
	 "name" text not null,
	 "weight" double null,
	 "is_agressive" bool default false not null )
	 ;

2. Export table DDL to a file:

   .. code-block:: postgres

	COPY (SELECT GET_DDL('cool_animals')) TO '/home/rhendricks/animals.ddl';

**Views**

1. List all views:

   .. code-block:: psql

	SELECT view_name FROM sqream_catalog.views;
   
	view_name             
	----------------------
	angry_animals         
	only_agressive_animals


2. Get the DDL for a view:

   .. code-block:: psql

	SELECT GET_VIEW_DDL('angry_animals');
	CREATE VIEW "public".angry_animals as
	   SELECT
		 "cool_animals"."id" as "id",
		 "cool_animals"."name" as "name",
		 "cool_animals"."weight" as "weight",
		 "cool_animals"."is_agressive" as "is_agressive"
	   FROM
		 "public".cool_animals as cool_animals
	   WHERE
		 "cool_animals"."is_agressive" = false;

3. Export view DDL to a file:

   .. code-block:: postgres

	COPY (SELECT GET_VIEW_DDL('angry_animals')) TO '/home/rhendricks/angry_animals.sql';

**User defined functions**

1. List all UDFs:

   .. code-block:: postgres
   
	SELECT * FROM sqream_catalog.user_defined_functions;

	database_name | function_id | function_name
	--------------+-------------+--------------
	master        |           1 | my_distance  

2. Get the DDL for a function:

   .. code-block:: postgres

	CREATE FUNCTION "my_distance" (x1 DOUBLE, y1 DOUBLE, x2 DOUBLE, y2 DOUBLE) 
	RETURNS DOUBLE AS $$ 
	SELECT CASE 
	WHEN y1 < x1 then 0.0 
		ELSE sqrt(power(y2 - y1, 2) + power(x2 - x1, 2)) 
		END; 
	$$ LANGUAGE SQL

3. Export function DDL to a file:

   .. code-block:: postgres

	COPY (SELECT GET_FUNCTION_DDL('my_distance')) TO '/home/rhendricks/my_distance.sql';

Dumping Entire Database DDLs
============================

Dumping the database DDL includes tables and views, but not UDFs and saved queries.

1. Export database DDL to a client:

   .. code-block:: postgres

	SELECT DUMP_DATABASE_DDL();
	CREATE TABLE "public"."cool_animals" (
	  "id" int not null,
	  "name" text not null,
	  "weight" double null,
	  "is_agressive" bool default false not null
	)
	;

	CREATE VIEW "public".angry_animals AS
	  SELECT
		  "cool_animals"."id" AS "id",
		  "cool_animals"."name" AS "name",
		  "cool_animals"."weight" AS "weight",
		  "cool_animals"."is_agressive" AS "is_agressive"
		FROM
		  "public".cool_animals as cool_animals
		WHERE
		  "cool_animals"."is_agressive" = false;

2. Export database DDL to a file:

   .. code-block:: postgres

	COPY (SELECT DUMP_DATABASE_DDL()) TO '/home/rhendricks/database.ddl';


To export data in tables, see :ref:`copy_to`

For more information, see :ref:`get_ddl`, :ref:`get_view_ddl`, :ref:`get_function_ddl`, :ref:`dump_database_ddl` 