.. _cpp_native:

*************************
C++ Native Driver
*************************

The SQream DB C++ driver allows C++ applications and tools connect to SQream DB.
This tutorial shows you how to write a C++ application using the native driver.

.. contents:: In this topic:
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

You can place the ``libsqream.so*`` files and ``sqream.h`` where you write your application, or copy them to the system ``lib`` and ``includes`` directories.

Examples
==============================================

Assuming you have an existing SQream DB instance to connect to, we'll connect to it using the application and run some statements.

Creating a table and inserting some values
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

   $ g++ -std=c++11 connect_test.cpp -lsqream -o connect_test
   $ ./connect_test
