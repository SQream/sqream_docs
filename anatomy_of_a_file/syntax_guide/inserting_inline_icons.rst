.. _inserting_inline_icons:

***********************
Inserting Inline Icons
***********************
Inserting inline icons refers to including a graphical icon in a sentence. You do this by inserting two syntactical elements into your page, as in the following example:

.. code-block:: console

   The **Data Encryption** page |icon-new_2022.1| describes the following:

You must include the following syntax somewhere on the page for the inline reference above to display the icon:

.. code-block:: console

   .. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
      :align: middle
      :width: 110