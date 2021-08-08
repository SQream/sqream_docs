.. _r:

*****************************
Connecting to SQream using R
*****************************

You can use R to interact with a SQream DB cluster.

This tutorial is a guide that will show you how to connect R to SQream DB.

.. contents:: In this topic:
   :local:

JDBC
=========


#. Get the :ref:`SQream DB JDBC driver<java_jdbc>`.

#. 
   In R, install RJDBC
   
   .. code-block:: rconsole
      
      > install.packages("RJDBC")
      Installing package into 'C:/Users/r/...'
      (as 'lib' is unspecified)

      package 'RJDBC' successfully unpacked and MD5 sums checked

#.
   Import the RJDBC library
   
   .. code-block:: rconsole
   
      > library(RJDBC)

#. 
   Set the classpath and initialize the JDBC driver which was previously installed. For example, on Windows:

   .. code-block:: rconsole
      
      > cp = c("C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
      > .jinit(classpath=cp)
      > drv <- JDBC("com.sqream.jdbc.SQDriver","C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
#. 
   Open a connection with a :ref:`JDBC connection string<connection_string>` and run your first statement
   
   .. code-block:: rconsole
   
      > con <- dbConnect(drv,"jdbc:Sqream://127.0.0.1:3108/master;user=rhendricks;password=Tr0ub4dor&3;cluster=true")
      
      > dbGetQuery(con,"select top 5 * from t")
         xint  xtinyint xsmallint xbigint 
      1    1       82      5067       1 
      2    2       14      1756       2 
      3    3       91     22356       3 
      4    4       84     17232       4 
      5    5       13     14315       5 

#. 
   Close the connection
   
   .. code-block:: rconsole
   
      > close(con)

A full example
-----------------

.. code-block:: rconsole

   > library(RJDBC)
   > cp = c("C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
   > .jinit(classpath=cp)
   > drv <- JDBC("com.sqream.jdbc.SQDriver","C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
   > con <- dbConnect(drv,"jdbc:Sqream://127.0.0.1:3108/master;user=rhendricks;password=Tr0ub4dor&3;cluster=true")
   > dbGetQuery(con,"select top 5 * from t")
      xint  xtinyint xsmallint xbigint 
   1    1       82      5067       1 
   2    2       14      1756       2 
   3    3       91     22356       3 
   4    4       84     17232       4 
   5    5       13     14315       5 
   > close(con)

ODBC
=========

#. Install the :ref:`SQream DB ODBC driver<odbc>` for your operating system, and create a DSN.

#. 
   In R, install RODBC
   
   .. code-block:: rconsole
      
      > install.packages("RODBC")
      Installing package into 'C:/Users/r/...'
      (as 'lib' is unspecified)

      package 'RODBC' successfully unpacked and MD5 sums checked

#.
   Import the RODBC library
   
   .. code-block:: rconsole
   
      > library(RODBC)

#. 
   Open a connection handle to an existing DSN (``my_cool_dsn`` in this example)

   .. code-block:: rconsole
      
      > ch <- odbcConnect("my_cool_dsn",believeNRows=F)

#. 
   Run your first statement
   
   .. code-block:: rconsole
   
      > sqlQuery(ch,"select top 5 * from t")
         xint  xtinyint xsmallint xbigint 
      1    1       82      5067       1 
      2    2       14      1756       2 
      3    3       91     22356       3 
      4    4       84     17232       4 
      5    5       13     14315       5 

#. 
   Close the connection
   
   .. code-block:: rconsole
   
      > close(ch)

A full example
-----------------

.. code-block:: rconsole

   > library(RODBC)
   > ch <- odbcConnect("my_cool_dsn",believeNRows=F)
   > sqlQuery(ch,"select top 5 * from t")
      xint  xtinyint xsmallint xbigint 
   1    1       82      5067       1 
   2    2       14      1756       2 
   3    3       91     22356       3 
   4    4       84     17232       4 
   5    5       13     14315       5 
   > close(ch)
