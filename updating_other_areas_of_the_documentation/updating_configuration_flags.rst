.. _updating_configuration_flags:

***********************
Updating Configuration Flags
***********************
Because some new features are set with configuration flags, new configuration flags must be added in the following places:

* The correct location on the `Configuration Flags <https://docs.sqream.com/en/latest/configuration_guides/configuration_flags.html>`_ page:

  * **Administration Flags:**

    * Regular Administration flags
    * Cluster Administration flags
    * Worker Administration flags

  * **Generic flags:**

    * Regular Generic flags
    * Worker Generic flags

    The **Development** team decides how to categorize the above flags, each of which is described in the shared `Configuration Flags - Final Review <https://docs.google.com/spreadsheets/d/1HojnqJdK7_ueJc0gLyK-o0Ig_XAzDxBC430eFuk6LGQ/edit#gid=0>`_ spreadsheet.

* On the page belonging to the specific flag. If the flag page does not exist (such as for new flags), you must create it.

* In the table located on the `All Configurations page <https://docs.sqream.com/en/latest/configuration_guides/current_method_all_configurations.html>`_

.. note:: The above changes must be made on **every branch**. The best way to do this is to keep a current local version of all documentation, and to add the required files (and/or folders) to every live branch **that it applies to**. Remember to modify all absolute links in accordance with the branch that you're copying the files into.

.. warning:: You should not add features introduced in a later branch to any preceding branches! This will allow front-end users without access to search for feature descriptions on branches that do not provide those features! That's what we call a "big no-no".