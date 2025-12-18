.. _text_to_array:

*********
TEXT_TO_ARRAY
*********

The ``TEXT_TO_ARRAY`` function converts a delimited text value into an array of strings using the specified delimiter.

Syntax
======

.. code-block:: postgres

   cast_utils.text_to_array(text_column,delimiter)

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``text_column``
     - The input string to be split into array elements.
   * - ``delimiter``
     - The string used as a separator between elements in text_column.

Returns
=======

* One array value per input row

* Each element in the returned array corresponds to a substring of text_column separated by delimiter.

* Returns a single-element array when the delimiter is not found; returns ``NULL`` if the input text or delimiter is ``NULL``.

.. note:: To use this function, the cupy package must be installed on each machine using a standard pip installation.

Examples
========

For these examples, assume a table named ``authors_books``, with the following structure:

.. code-block:: postgres

   CREATE OR REPLACE TABLE authors_books (
       author_name TEXT,
       books       TEXT
   );

   INSERT INTO authors_books (author_name, books) VALUES
       ('George Orwell', '1984,Animal Farm,Homage to Catalonia'),
       ('J.K. Rowling', 'Harry Potter and the Sorcerer''s Stone,Harry Potter and the Chamber of Secrets,Harry Potter and the Prisoner of Azkaban'),
       ('J.R.R. Tolkien', 'The Hobbit,The Fellowship of the Ring,The Two Towers,The Return of the King'),
       ('Agatha Christie', 'Murder on the Orient Express,And Then There Were None,Death on the Nile'),
       ('Isaac Asimov', 'Foundation,I Robot,The Caves of Steel');

		
Converting A Text Into Array
----------------------------

.. code-block:: psql

   test=> select cast_utils.text_to_array(books,',') from authors_books  ;
   text_to_array
   ------------------------------------------------------------------------------------------------------------------------------
   ["1984","Animal Farm","Homage to Catalonia"]     
   ["Harry Potter and the Sorcerer's Stone","Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban"]      
   ["The Hobbit","The Fellowship of the Ring","The Two Towers","The Return of the King"]          
   ["Murder on the Orient Express","And Then There Were None","Death on the Nile"]      
   ["Foundation","I Robot","The Caves of Steel"]     

Using Array Functions over Text To Array
----------------------------------------

Usage for array_length,implicitly indexing and Unnest

.. code-block:: psql

   test=>  select unnest(cast_utils.text_to_array(b.books,',')) from authors_books b where array_length(cast_utils.text_to_array(b.books,','))>2 and cast_utils.text_to_array(b.books,',')[1]='I Robot'  ;
   unnest 
   ----------
   Foundation
   I Robot
   The Caves of Steel

