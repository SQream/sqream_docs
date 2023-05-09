.. _creating_a_database:

****************************
Creating a Database
****************************
Once you've installed SQream you can create a database.

**To create a database:**

1. Write a :ref:`create_database` statement.

   The following is an example of creating a new database:

   .. code-block:: psql

      master=> CREATE DATABASE test;
      executed

2. Reconnect to the newly created database.

   1. Exit the client by typing ``\q`` and pressing **Enter**.
   2. From the Linux shell, restart the client with the new database name:

      .. code-block:: psql

         $ sqream sql --port=5000 --username=rhendricks -d test
         Password:
   
         Interactive client mode
         To quit, use ^D or \q.
   
         test=> _

    The name of the new database that you are connected to is displayed in the prompt.