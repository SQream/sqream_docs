.. _running_the_sqream_sql_client:

****************************
Running the SQream SQL Client
****************************
The following example shows how to run the SQream SQL client:

.. code-block:: console

   $ sudo java -jar jdbc-console-*.*.**.jar --host=<SQream cluster IP address>

     Welcome to JDBC console
     To quit, use ^C or exit

     Connection URL
	 
     jdbc:Sqream://<SQream cluster IP address>:<SQream cluster port>/master;user=<username>;password=<password>;cluster=false
     master=> _

Running the SQream SQL client prompts you to provide your password. Use the username and password that you have set up, or your DBA has provided.
  
.. tip::
   * You can exit the shell by typing ``exit`` or :kbd:`Ctrl-c`. 
   * A new SQream cluster contains a database named `master,` which is the database used in the examples on this page.