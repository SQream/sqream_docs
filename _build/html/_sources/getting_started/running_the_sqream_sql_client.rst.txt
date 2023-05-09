.. _running_the_sqream_sql_client:

****************************
Running the SQream SQL Client
****************************
The following example shows how to run the SQream SQL client:

.. code-block:: psql

   $ sqream sql --port=5000 --username=rhendricks -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

Running the SQream SQL client prompts you to provide your password. Use the username and password that you have set up, or your DBA has provided.
  
.. tip::
   * You can exit the shell by typing ``\q``  or :kbd:`Ctrl-d`. 
   * A new SQream cluster contains a database named `master,` which is the database used in the examples on this page.