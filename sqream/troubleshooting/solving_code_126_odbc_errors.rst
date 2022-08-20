.. _solving_code_126_odbc_errors:

***********************
Solving "Code 126" ODBC Errors
***********************
After installing the ODBC driver, you may experience the following error: 

.. code-block:: none

   The setup routines for the SQreamDriver64 ODBC driver could not be loaded due to system error
   code 126: The specified module could not be found.
   (c:\Program Files\SQream Technologies\ODBC Driver\sqreamOdbc64.dll)

This is an issue with the Visual Studio Redistributable packages. Verify you've correctly installed them, as described in the :ref:`Visual Studio 2015 Redistributables <vcredist>` section above.
