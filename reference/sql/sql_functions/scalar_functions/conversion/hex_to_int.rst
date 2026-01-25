.. _hex_to_int:

**********
HEX_TO_INT
**********

The ``hex_to_int`` function converts a hexadecimal number into its signed 32-bit integer (INT) representation.

Syntax
======

.. code-block:: postgres

   cast_utils.hex_to_int(hex_string)

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``hex_string``
     - A string representing a hexadecimal number. The value may optionally include the ``0x`` prefix.

Return
=======

* Returns the decimal (base-10) integer value represented by the input hexadecimal string.

* ``NULL`` input returns ``NULL``. Invalid input results in an error.

* The maximum supported hexadecimal value is ``0x7FFFFFFF`` and will return ``2,147,483,647``. Any hexadecimal value greater than ``0x7FFFFFFF`` results in an error.

.. note:: This feature supports hexadecimal conversion to INT only. Conversion to BIGINT is not supported.

Examples
========

For this example, assume a table named ``sensor_readings``, with the following structure:

.. code-block:: postgres

   CREATE TABLE sensor_readings (
    sensor_name text,
    hex_payload text,
    recorded_at timestamp
	);

   INSERT INTO sensor_readings (sensor_name, hex_payload, recorded_at )
	VALUES 
		('Living Room', '0x1E','2026-11-01 01:24:00.000'),
		('Kitchen',     '22','2026-11-01 02:25:00.000'),
		('Bedroom',     '1A','2026-11-01 03:26:00.000');

		
Converting A Hexadecimal String Into An Integer
-----------------------------------------------

.. code-block:: psql

   test=> SELECT sensor_name,
			hex_payload AS raw_hex, 
			cast_utils.hex_to_int(hex_payload) AS temp_celsius, 
		   (cast_utils.hex_to_int(hex_payload) * 9/5) + 32 AS temp_fahrenheit,
		    recorded_at
		  FROM sensor_readings;

	+-----------+-------+------------+---------------+-----------------------+
	|sensor_name|raw_hex|temp_celsius|temp_fahrenheit|recorded_at            |
	+-----------+-------+------------+---------------+-----------------------+
	|Living Room|1E     |30          |86             |2026-11-01 01:24:00.000|
	+-----------+-------+------------+---------------+-----------------------+
	|Kitchen    |22     |34          |93             |2026-11-01 02:25:00.000|
	+-----------+-------+------------+---------------+-----------------------+
	|Bedroom    |1A     |26          |78             |2026-11-01 03:26:00.000|
	+-----------+-------+------------+---------------+-----------------------+



	
