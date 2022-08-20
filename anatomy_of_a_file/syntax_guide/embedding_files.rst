.. _embedding_files:

***********************
Embedding Files
***********************
**Embedding files** refers to a syntax that you insert into a page to show a saved .txt file, and is basically identical to the concept of **content reuse**.

.. note:: The file that you refer to with the embedded file syntax must be located in the same folder containing the file in which the syntax is placed.

The following is the embedded file syntax:

.. code-block:: console

   .. literalinclude:: test.php
        :language: php
        :emphasize-lines: 4
        :linenos:

The following is the text of the embedded file:

.. literalinclude:: test.php
     :language: php
     :emphasize-lines: 4
     :linenos:

Notice that the **fourth line** in the text above is highlighted. You can highlight lines using the ``:emphasize-lines: 4`` syntax, as shown in the syntax example above.