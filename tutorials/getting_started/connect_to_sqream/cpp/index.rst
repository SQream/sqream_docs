.. _cpp_native:

*************************
C++ Native Driver
*************************

The SQream DB C++ driver allows C++ applications and tools connect to SQream DB.
This tutorial shows you how to write a C++ application using the native driver.

.. contents:: In this topic:
   :depth: 2
   :local:


Installing the C++ driver
==================================

Prerequisites
----------------

The SQream DB C++ driver was built on 64-bit Linux, and is designed to work with RHEL 7 and Ubuntu 16.04 and newer.

Getting the library
---------------------

The C++ driver is provided as a tarball containing the compiled ``libsqream.so`` file and a header ``sqream.h``. Get the driver from the `SQream Drivers page <http://sqream.com/product/client-drivers>`_. The library can be integrated into your C++-based applications or projects.


Extract the tarball archive
-----------------------------

Extract the library files from the tarball

.. code-block:: console

   $ tar xf libsqream-3.0.tar.gz

Examples
==============================================

Assuming you have an existing SQream DB instance to connect to, we'll connect to it using the application and run some statements.

Testing the connection to SQream DB
--------------------------------------------
You can download this file by right clicking and saving to your computer :download:`connect_test.cpp <connect_test.cpp>`.

.. literalinclude:: connect_test.cpp
    :language: cpp
    :caption: Connect to SQream DB
    :linenos:


Compiling and running the application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build the C++ application, run the following command from the directory that contains the code and header file

.. code-block:: console

   $ g++ -Wall -Ilibsqream-3.0 -Llibsqream-3.0 -lsqream connect_test.cpp -o connect_test
   $ ./connect_test

Creating a table and inserting values
--------------------------------------------
You can download this file by right clicking and saving to your computer :download:`insert_test.cpp <insert_test.cpp>`.

.. literalinclude:: insert_test.cpp
    :language: cpp
    :caption: Inserting data to a SQream DB table
    :linenos:


Compiling and running the application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build the C++ application, run the following command from the directory that contains the code and header file

.. code-block:: console

   $ g++ -Wall -Ilibsqream-3.0 -Llibsqream-3.0 -lsqream insert_test.cpp -o insert_test
   $ ./insert_test

