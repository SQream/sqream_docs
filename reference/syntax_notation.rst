.. _syntax_notation:

*************************
Syntax Notation
*************************


.. list-table:: 
    :widths: auto
    :header-rows: 1
	
    * - Notation
      - Description
      - Example
    * - ``UPPERCASE``
      - Reserved words used as keywords in SQL statements. See full list :ref:`here<keywords_and_identifiers>`	
      - ``SELECT``
    * - ``lowercase``
      - User-defined identifiers such as table names, column names, aliases, and variables.
      - ``table_name``
    * - Arithmetic operators
      - Used to perform mathematical operations on numeric values. See full list :ref:`here<arithmetic_operators>`
      - ``%``
    * - Comparison operators
      - Used to compare values or expressions and determine their relationship or equality within SQL statements. See full list :ref:`here<scalar_expressions>`
      - ``=>``
    * - ``""``
      - Double quotes are used to enclose identifiers that contain special characters or reserved keywords
      - ``SELECT * FROM "order";``
    * - ``<>``
      - Angle brackets are used to represent placeholders or user-defined elements in SQL statements
      - ``<user_name>``
    * - ``[]``
      - Square brackets are used as syntax notation to indicate optional inputs
      - ``GRANT LOGIN TO <role1> [, ...]``
    * - ``|``
      - The vertical bar is used to indicate a choice or alternative between different options. It signifies that only one option should be selected from the given set of possibilities.
      - ``GRANT { SUPERUSER | LOGIN | PASSWORD '<password>' } TO <role>``
    * - ``{}``
      - The curly brackets are used to group options or parameters together. They indicate that the elements inside the brackets are choices, and you can select only one of them
      - ``GRANT { SUPERUSER | LOGIN | PASSWORD '<password>' } TO <role>``
	    
	  

	  
	  
	  
