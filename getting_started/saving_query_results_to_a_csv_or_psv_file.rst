.. _saving_query_results_to_a_csv_or_psv_file:

****************************
Saving Query Results to a CSV or PSV File
****************************
You can save query results to a CSV or PSV file using the ``sqream sql`` command from a CLI client. This saves your query results to the selected delimited file format, as shown in the following example:

.. code-block:: console

   $ sudo java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address] -c "SELECT * FROM nba LIMIT 5" --results-only --delimiter='|' > nba.psv
   $ cat nba.psv
   Avery Bradley           |Boston Celtics        |0|PG|25|6-2 |180|Texas                |7730337
   Jae Crowder             |Boston Celtics        |99|SF|25|6-6 |235|Marquette            |6796117
   John Holland            |Boston Celtics        |30|SG|27|6-5 |205|Boston University    |\N
   R.J. Hunter             |Boston Celtics        |28|SG|22|6-5 |185|Georgia State        |1148640
   Jonas Jerebko           |Boston Celtics        |8|PF|29|6-10|231|\N|5000000

For more output options, see :ref:`Controlling the Client Output<controlling_output>`.

.. rubric:: What's next?

* Explore all of SQream DB's :ref:`SQL Syntax <sql_syntax>`.
* See the full :ref:`SQream SQL CLI reference <sqream_sql_cli_reference>`.
* Connect a :ref:`third party tool <third_party_tools>` to start analyzing data.