.. _literals:

***************************
Literals
***************************

Literals represent constant values.

SQream DB contains several types of literals:

* :ref:`Number literals<number_literals>` - define numbers such as ``1.3``, ``-5``
* :ref:`String literals<string_literals>` - define text values like ``'Foxes are cool'``, ``'1997-01-01'``
* :ref:`Typed literals<typed_literals>` - define values with explicit types like ``(3.0 :: float)``
* :ref:`Other constants<constants>` - predfined values like ``NULL`` or ``TRUE``

.. _number_literals:

Number literals
===================

A number literal can be expressed in the following way:

.. code-block:: postgres

   number_literal ::=
      [+-] digits
      | digits . [ digits ] [ e [+-] digits ]
      | [ digits ] . digits [ e [+-] digits ]
      | digits e[+-]digits


Examples
------------

.. code-block:: postgres

   1234

   1234.56

   12.

   .34

   123.56e-45

   0.23
   
   3.141
   
   42

.. note:: 
   The actual data type of the value changes based on context, the format used, and the value itself.
   For example, any number containing the decimal point will be considered ``FLOAT`` by default.
   Any whole number will considered ``INT``, unless the value is larger than the :ref:`maximum value<data_types>`, in which case the type will become a ``BIGINT``.

.. _string_literals:

String literals
==================

String literals are string (text) values, encoded either in ASCII or UTF-8.

A string literal is quoted with single quotes (``'``) or dollars (``$$``)

.. tip:: To use a single quote in a string, repeat the single quote twice. See examples below.


Examples
------------

.. code-block:: postgres
   
   'This is an example of a string'
   
   'Hello? Is it me you''re looking for?' -- Repeated single quotes are treated as a single quote
   
   $$That is my brother's company's CEO's son's dog's toy$$ -- Dollar-quoted
   
   '1997-01-01' -- This is a string


The actual data type of the value changes based on context, the format used, and the value itself. In the example below, the first value is interpreted as a ``DATE``, while the second is interpreted as a ``VARCHAR``.

.. code-block:: postgres

   INSERT INTO cool_dates(date_col, reason) VALUES ('1955-11-05', 'Doc Brown discovers flux capacitor');

.. _typed_literals:

Typed literals
================

A typed literal allows the creation of any data type using either of the following syntaxes:

.. code-block:: postgres
   
   CAST(literal AS type_name)
   -- or
   literal :: type_name

Syntax reference
-------------------

   typed_literal ::=
         CAST(literal AS type_name)
         | literal :: type_name

.. code-block:: postgres
   
   typed_literal ::=
         cast(literal AS type_name)
         | literal :: type_name
   
   literal ::=
         string_literal
         | number_literal
         | NULL | TRUE | FALSE

   type_name ::=

       BOOL
       | TINYINT
       | SMALLINT
       | INT
       | BIGINT
       | FLOAT
       | REAL
       | DATE
       | DATETIME
       | VARCHAR ( digits )
       | NVARCHAR ( digits )


Examples
----------

.. code-block:: postgres
   
   '1955-11-05' :: date
   
   'TRUE' :: BOOL
   
   CAST('2300' as BIGINT)
   
   CAST(42 :: FLOAT)

.. _constants:

Other constants
================

* ``TRUE`` and ``FALSE`` are interpreted as values of type ``BOOL``.

* ``NULL`` - which has no type by itself. The type is inferred from context during query compilation.

