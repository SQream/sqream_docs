.. _menu_elements:

***********************
Topic Menu Elements
***********************
This section describes the following topic menu elements:

.. contents:: 
   :local:
   :depth: 1

Topic Menu Items
=================
Your **topic menu items** are the heading and sub-heading topics displayed on your left menu. You can create menu items using the ``toctree`` syntax.

For more information about creating menu items using this syntax, see :ref:`toc_tree`.

Menu Captions
=====================
**Menu captions** are the blue lines of text in the menu separating each area of documentation. You insert menu captions into the highest level index file using the ``:caption`` syntax:

.. code-block::

   .. toctree::
      :maxdepth: 4
      :caption: In The Beginning...
      :glob: