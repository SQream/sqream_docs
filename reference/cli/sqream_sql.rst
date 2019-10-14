.. _sqream_sql_cli_reference:

*****************************
SQream SQL (CLI) Reference
*****************************

SQream DB comes with a built-in client for executing SQL statements either interactively or from the command-line.

This page serves as a reference for the options and parameters. Learn more about the usage of the CLI by visiting the :ref:`tutorial page SQream SQL Client <sqream_sql_client>`.



Command line arguments
-----------------------

**SQream SQL** supports the following command line arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``-c`` or ``--command``
     - None
     - Changes the mode of operation to single-command, non-interactive. Use this argument to run a statement and immediately exit.
   * - ``-f`` or ``--file``
     - None
     - Changes the mode of operation to multi-command, non-interactive. Use this argument to run a sequence of statements from an external file and immediately exit.
   * - ``--host``
     - ``127.0.0.1``
     - Address of the SQream DB instance.
   * - ``--port``
     - ``5000``
     - Sets the connection port.
   * - ``--databasename`` or ``-d``
     - None
     - Specifies the database name for queries and statements in this session.
   * - ``--username``
     - None
     -  Username to connect to the specified database.
   * - ``--password``
     - None
     - Specify the password using the command line argument. If not specified, the client will prompt the user for the password.
   * - ``--clustered``
     - False
     - When used, the client connects to the load balancer, usually on port ``3108``. If not set, the client assumes the connection is to a standalone SQream DB instance.
   * - ``--service``
     - ``sqream``
     - Service name (queue) that statements will file into.
   * - ``--results-only``
     - False
     - Outputs results only, without timing information and row counts
   * - ``--no-history``
     - False
     - When set, prevents command history from being saved in ``~/.sqream/clientcmdhist``

.. tip:: Run ``$  ClientCmd --help`` to see a full list of arguments


Meta-commands
----------------

* Meta-commands in SQream SQL start with a backslash (``\``)

.. note:: Meta commands do not end with a semicolon

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Example
     - Description
   * - ``\q`` or ``\quit``
     - .. code-block:: psql
          
            master=> \q
     - Quit the client. (Same as :kbd:`Ctrl-d`)
   * - ``\c <database>`` or ``\connect <database>``
     - .. code-block:: psql
          
            master=> \c fox
            fox=>
     - Changes the current connection to an alternate database

Basic Commands
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-l`
     - Clear the screen.
   * - :kbd:`Ctrl-c`
     - Terminate the current command.
   * - :kbd:`Ctrl-z`
     - Suspend/stop the command.
   * - :kbd:`Ctrl-d`
     - Quit SQream SQL



Moving about the command line
---------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-a`
     - go to the start of the command line 
   * - :kbd:`Ctrl-e`
     - go to the end of the command line 
   * - :kbd:`Ctrl-k`
     - delete from cursor to the end of the command line 
   * - :kbd:`Ctrl-u`
     - delete from cursor to the start of the command line 
   * - :kbd:`Ctrl-w`
     - delete from cursor to start of word (i.e. delete backwards one word) 
   * - :kbd:`Ctrl-y`
     - paste word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor 
   * - :kbd:`Alt-b`
     - move backward one word (or go to start of word the cursor is currently on)
   * - :kbd:`Alt-f`
     - move forward one word (or go to end of word the cursor is currently on) 
   * - :kbd:`Alt-d`
     - delete to end of word starting at cursor (whole word if cursor is at the beginning of word) 
   * - :kbd:`Alt-c`
     - capitalize to end of word starting at cursor (whole word if cursor is at the beginning of word) 
   * - :kbd:`Alt-u`
     - make uppercase from cursor to end of word 
   * - :kbd:`Alt-l`
     - make lowercase from cursor to end of word 
   * - :kbd:`Ctrl-f`
     - move forward one character 
   * - :kbd:`Ctrl-b`
     - move backward one character 
   * - :kbd:`Ctrl-h`
     - delete character before the cursor 
   * - :kbd:`Ctrl-t`
     - swap character under cursor with the previous one

Searching
------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-r`
     - search the history backwards
   * - :kbd:`Ctrl-g`
     - escape from history searching mode
   * - :kbd:`Ctrl-p`
     - previous command in history (i.e. walk back through the command history)
   * - :kbd:`Ctrl-n`
     - next command in history (i.e. walk forward through the command history)