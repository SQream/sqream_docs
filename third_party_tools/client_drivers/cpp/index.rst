.. _cpp_native:

*************************
C++ Driver
*************************

The SQream DB C++ driver allows C++ programs and tools to connect to SQream DB.

This tutorial shows how to write a C++ program that uses this driver.

.. contents:: In this topic:
   :depth: 2
   :local:


Installing the C++ Driver
==================================

Prerequisites
----------------

The SQream DB C++ driver was built on 64-bit Linux, and is designed to work with RHEL 7 and Ubuntu 16.04 and newer.

Getting the Library
---------------------

The C++ driver is provided as a tarball containing the compiled ``libsqream.so`` file and a header ``sqream.h``. Get the driver from the `SQream Drivers page <https://docs.sqream.com/en/v2020-2/third_party_tools/client_drivers/index.html>`_. The library can be integrated into your C++-based applications or projects.


Extract the Tarball Archive
-----------------------------

Extract the library files from the tarball

.. code-block:: console

   $ tar xf libsqream-3.0.tar.gz

Examples
==============================================

Assuming there is a SQream DB worker to connect to, we'll connect to it using the application and run some statements.

Testing the Connection to SQream
--------------------------------------------

Download this file by right clicking and saving to your computer :download:`connect_test.cpp <connect_test.cpp>`.

.. literalinclude:: connect_test.cpp
    :language: cpp
    :caption: Connect to SQream DB
    :linenos:


Compiling and Running the Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build this code, place the library and header file in ./libsqream-3.0/ and run

.. code-block:: console

   $ g++ -Wall -Ilibsqream-3.0 -Llibsqream-3.0 -lsqream connect_test.cpp -o connect_test
   $ ./connect_test

Modify the ``-I`` and ``-L`` arguments to match the ``.so`` library and ``.h`` file if they are in another directory.

Creating a Table and Inserting Values
--------------------------------------------

Download this file by right clicking and saving to your computer :download:`insert_test.cpp <insert_test.cpp>`.

.. literalinclude:: insert_test.cpp
    :language: cpp
    :caption: Inserting data to a SQream DB table
    :linenos:


Compiling and Running the Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build this code, use

.. code-block:: console

   $ g++ -Wall -Ilibsqream-3.0 -Llibsqream-3.0 -lsqream insert_test.cpp -o insert_test
   $ ./insert_test