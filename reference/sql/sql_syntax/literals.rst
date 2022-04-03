.. _literals:

***************************
Literals
***************************


Literals represent constant values.

SQream DB contains the following types of literals:

* :ref:`Numeric literals<numeric_literals>` - define numbers such as ``1.3``, ``-5``
* :ref:`String literals<string_literals>` - define text values like ``'Foxes are cool'``, ``'1997-01-01'``
* :ref:`Typed literals<typed_literals>` - define values with explicit types like ``(3.0 :: float)``
* :ref:`Boolean literals<boolean_literals>` - define values that include ``true`` and ``false``
* :ref:`Other constants<constants>` - predefined values like ``NULL`` or ``TRUE``

.. _numeric_literals:

Numeric Literals
===================

**Numeric literals** can be expressed as follows:

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

.. note:: 
   A numeric literal that contains neither a decimal point nor an exponent is considered ``INT`` by default if its value fits in type ``INT`` (32 bits). If not, it is considered ``BIGINT`` by default if its value fits in type ``BIGINT`` (64 bits). If neither are true, it is considered ``FLOAT``. Literals that contain decimal points and/or exponents are always considered ``FLOAT``.

.. _string_literals:

String Literals
==================

**String literals** are string (text) values, encoded either in ASCII or UTF-8.

String literals are surrounded by single quotes (``'``) or dollars (``$$``)

.. tip:: To use a single quote in a string, use a repeated single quote.


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
   
This section describes the following types of literals:

* :ref:`Regular string literals<regular_literals>`
* :ref:`Dollar-quoted string literals<dollar_quoted_string_literals>`
* :ref:`Escaped string literals<escaped_string_literals>`


.. _regular_literals:

Regular String Literals
-----------------------
In SQL, a **regular string literal** is a sequence of zero or more characters bound by single quotes (``'``):

.. code-block:: postgres

   'This is a string'.
   
You can include a single-quote character in a string literal with two consecutive single quotes (``''``):

.. code-block:: postgres

   'Dianne''s horse'.

Note that two adjacent single quotes is not the same as a double-quote character (``"``).

Examples
------------

The following are some examples of regular string literals:

.. code-block:: postgres

   '123'

   'אבג'

   'a''b'

   ''

.. _dollar_quoted_string_literals:

Dollar-Quoted String Literals
-----------------------
**Dollar-quoted string literals** consist of a dollar sign (``$``), an optional "tag" of zero or more characters, another dollar sign, an arbitrary sequence of characters that make up the string content, a dollar sign, the same tag at the beginning of the dollar quote, and another dollar sign.


Examples
------------

For example, below are two different ways to specify the string ``Dianne's horse`` using dollar-quoted string literals:

.. code-block:: postgres

   $$Dianne's horse$$
   $<tag>$Dianne's horse$<tag>$
   
Note that you can use single quotes inside the dollar-quoted string without an escape. Because the string is always written literally, you do not need to escape any characters inside a dollar-quoted string. Backslashes and dollar signs indicate no specific functions unless they are part of a sequence matching the opening tag.

Any used tags in a dollar-quoted string follow the same rules as for unquoted identifiers, except that they cannot contain a dollar sign.

In addition, because tags are case sensitive, ``$<tag>$String content$<tag>$`` is correct, but ``$<TAG>$String content$<tag>$`` is incorrect.

A dollar-quoted string that follows a keyword or identifier must be separated from it by whitespace (such as spaces, tabs, or newlines). If you do not separate them with whitespace, the dollar-quoting delimiter is taken as part of the preceding identifier.

.. _escaped_string_literals:

Escaped String Literals
-----------------------
Because regular string literals do not support inserting special characters (such as new lines), the **escaped string literals** syntax was added to support inserting special characters with an escaping syntax.

In addition to being enclosed by single quotes (e.g. 'abc'), escaped string literals are preceded by a capital ``E``.

.. code-block:: postgres

   E'abc'

The character sequence inside the single quotes can contain escaped characters in addition to regular characters, shown below:

.. list-table::
   :widths: 25 85
   :header-rows: 1  
   
   * - Sequence
     - Interpretation
   * - ``\b``
     - Inserts a backspace.
   * - ``\f``
     - Inserts a form feed.
   * - ``\n``
     - Inserts a newline.
   * - ``\r``
     - Inserts a carriage return.
   * - ``\t``
     - Inserts a tab.	 
   * - ``\o``, ``\oo``, ```\ooo``` (``o`` = ``0`` - ``7``)
     - Inserts an octal byte value. This sequence is currently not supported.
   * - ``\xh``, ``\xhh`` (``h`` = ``0`` - ``9``, ``A`` - ``F``)
     - Inserts a hexadecimal byte value. This sequence is currently not supported.
   * - ``\uxxxx``, ``\Uxxxxxxxx``
     - Inserts a 16 or 32-bit hexadecimal unicode character value (x = 0 - 9, A - F).
	 
Excluding the characters in the table above, escaped string literals take all other characters following a backslash literally. To include a backslash character, use two consecutive backslashes (``\\``). You can use a single quote in an escape string by writing ``\'``, in addition to the normal method (``''``).

.. _typed_literals:

Typed Literals
================

**Typed literals** allow you to create any data type using either of the following syntaxes:

.. code-block:: postgres
   
   CAST(literal AS type_name)

.. code-block:: postgres

   literal :: type_name

See also :ref:`cast` for more information about supported casts.

Syntax Reference
-------------------
The following is a syntax reference for typed literals:

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
       | TEXT ( digits )

Examples
----------

.. code-block:: postgres
   
   '1955-11-05' :: date
   
   'TRUE' :: BOOL
   
   CAST('2300' as BIGINT)
   
   CAST(42 :: FLOAT)

.. _boolean_literals:
   
Boolean Literals
===================
**Boolean literals** include the keywords ``true`` or ``false``.

Example
----------

.. code-block:: postgres

   INSERT INTO animals VALUES ('fox',true), ('cat',true), ('kiwi',false);

.. _constants:

Other Constants
================

The following other constants can be used:

* ``TRUE`` and ``FALSE`` - interpreted as values of type ``BOOL``.
* ``NULL`` - which has no type of its own. The type is inferred from context during query compilation.
