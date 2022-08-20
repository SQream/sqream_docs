.. _local_toc:

***********************
Creating a Local Table of Contents
***********************
The following syntax is used for creating a local table of contents (TOC):

.. code-block:: console

   .. contents:: 
      :local:
      :depth: 1

The local TOC is created based on the headings on your page. The ``:local:`` syntax includes all headings under your main title in the TOC. The ``:depth:`` syntax defines how many heading levels to include in your TOC. For example a depth of ``1`` displays only first level headings, ``2`` includes second level headings, and so on.

.. note:: Your TOC can only display headings that are included on the page. If you set your depth to 2, but don't have any second level headings, they will not be displayed in your TOC.
