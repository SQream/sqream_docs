.. _r:

*****************************
Connect to SQream Using R
*****************************

Overview
=========
The **R** programming language is used for statistical computing and graphics data analysis. The **Connect to SQream using R** page explains how to connect to a SQream cluster, and describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Prerequisites
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Installing Informatica Cloud Services
-------------------
The **Installing Informatica Cloud Services** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Installing and Setting Up the JDBC Driver
~~~~~~~~~~~~~~~
**To install and set up the JDBC driver:**

1. Download the JDBC driver installer from the `SQream Drivers page <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    ::

#. In R, install the **RJDBC package**: **Comment** - Why do we say, "In R"? Isn't the entire procedure done in R?
   
   .. code-block:: rconsole
      
      > install.packages("RJDBC")
      Installing package into 'C:/Users/r/...'
      (as 'lib' is unspecified)

      package 'RJDBC' successfully unpacked and MD5 sums checked

#. Import the **RJDBC library**:
   
   .. code-block:: rconsole
   
      > library(RJDBC)

#. Set the classpath and initialize the JDBC driver that you installed.

   The following is an example of setting the classpath and initializing the JDBC driver on Windows:

   .. code-block:: rconsole
      
      > cp = c("C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
      > .jinit(classpath=cp)
      > drv <- JDBC("com.sqream.jdbc.SQDriver","C:\\Program Files\\SQream Technologies\\JDBC Driver\\2020.1-3.2.0\\sqream-jdbc-3.2.jar")
	  
#. Open a connection using a connection string and run a statement:

   .. code-block:: rconsole
   
      > con <- dbConnect(drv,"jdbc:Sqream://127.0.0.1:3108/master;user=rhendricks;password=Tr0ub4dor&3;cluster=true")
      
      > dbGetQuery(con,"select top 5 * from t")
         xint  xtinyint xsmallint xbigint 
      1    1       82      5067       1 
      2    2       14      1756       2 
      3    3       91     22356       3 
      4    4       84     17232       4 
      5    5       13     14315       5 
	  
   For more information about connection strings, see `Connection String Examples <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html#connection-string-examples>`_.

#. Close the connection:
   
   .. code-block:: rconsole
   
      > close(con)

   The following is an example of installing and setting up the JDBC driver:

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

Installing and Setting Up the ODBC Driver
~~~~~~~~~~~~~~~
**To install and set up the ODBC driver:**

#. Download the JDBC driver installer from the `SQream Drivers page <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.
 
    ::
	
#. Create a DSN.

    ::
	
#. In R, install the **RODBC package**: **Comment** - Why do we say, "In R"? Isn't the entire procedure done in R?
   
   .. code-block:: rconsole
      
      > install.packages("RODBC")
      Installing package into 'C:/Users/r/...'
      (as 'lib' is unspecified)

      package 'RODBC' successfully unpacked and MD5 sums checked

#. Import the **RODBC library**:
   
   .. code-block:: rconsole
   
      > library(RODBC)

#. Open a connection handle to an existing DSN.

   The following example shows how to open a connection handle to an existing DSN to a handle called **my_cool_dsn**:

   .. code-block:: rconsole
      
      > ch <- odbcConnect("my_cool_dsn",believeNRows=F)

#. Run a statement:
   
   .. code-block:: rconsole
   
      > sqlQuery(ch,"select top 5 * from t")
         xint  xtinyint xsmallint xbigint 
      1    1       82      5067       1 
      2    2       14      1756       2 
      3    3       91     22356       3 
      4    4       84     17232       4 
      5    5       13     14315       5 

#. Close the connection:
   
   .. code-block:: rconsole
   
      > close(ch)

   The following is an example of installing and setting up the ODBC driver:

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
   
Configuring Informatica Cloud Services
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Launching Informatica Cloud Services
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Operating Informatica Cloud Services
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Troubleshooting Informatica Cloud Services
-------------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.