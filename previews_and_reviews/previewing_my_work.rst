.. _previewing_my_work:

***********************
How Do I Preview My Work Before Publishing It?
***********************
You can preview your work using a **build file**, which is a file that you can quickly generate to preview your changes on the front end. It is highly recommended to generate this file over and over until your page looks correct and all links function exactly as needed. The additional benefit of the build file is that applying changes to a live branch takes about five minutes for the changes to be published, while generating a build file takes about five seconds. 

**How to generate a build file:**

1. Open the **Command Line Interface (CLI)**, also known as the **Command Prompt**.

   The CLI shows this line:

   .. code-block:: console

      C:\Users\Yaniv>

       ::

2. Navigate to the **sqream_docs** repository as follows:

   .. code-block:: console

      C:\Users\Yaniv>cd sqream_docs

   In the example above, **cd** stands for **change directory** and is used to navigate to your desired directory. You can type ``cd ..`` to move backward in the directory in the CLI.

3. Type **make html -Q** to generate the build file.

   An output similar to the following is generated:

   .. code-block:: console
   
      C:\Users\Yaniv\sqream_docs\troubleshooting\tableau_related_issues.rst:69: WARNING: Literal block expected; none found.
      looking for now-outdated files... none found
      pickling environment... done
      checking consistency... C:\Users\Yaniv\sqream_docs\architecture\processes_and_network_architecture.rst: WARNING: document isn't included in any toctree
      C:\Users\Yaniv\sqream_docs\configuration_guides\bin_sizes.rst: WARNING: document isn't included in any toctree
      C:\Users\Yaniv\sqream_docs\configuration_guides\cache_disk_dir.rst: WARNING: document isn't included in any toctree

   .. note:: You do not need to modify your content in the event of a WARNING, as shown in the example above. These warnings do not affect the outcome of your page.

   .. tip:: When generating a build file, make sure that you navigate to the repository containing the pages you want to preview (step 2).
