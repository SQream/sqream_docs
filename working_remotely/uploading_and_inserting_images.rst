.. _uploading_and_inserting_images:

***********************
How to Upload and Insert Images
***********************
This section describes how to upload and insert images on your remote GitHub:

**To insert images on your remote GitHub:**

1. On your local computer, save your image(s) in the **_static** folder.

   This lets you easily transfer images to all required branch folders. Note that you can also save a folder of images.

2. Access a repository and branch, and click the _static folder, where all images are stored.

    ::

3. Click **Add file**.

    ::

4. Click **Upload files**.

    ::

5. Drag or select your image file(s) from your hard drive into the folder region.

    ::

6. Insert the image syntax shown below into the location on the page you want the image to be displayed:

   .. code-block:: console

      .. image:: /_static/<folder>/<image_file_name>.png

   The following is an example of the image syntax:

   .. code-block:: console

      .. image:: /_static/images/dashboard.png

7. Generate and check your build file.

    ::

8. Push and commit your changes.

.. note::  Verify that **Commit directly to the <branch name> branch** is selected. This option is selected by default.
