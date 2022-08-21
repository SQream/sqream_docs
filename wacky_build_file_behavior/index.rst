.. _wacky_build_file_behavior:

***********************
Why Is My Build File Menu Not Working Right?
***********************
A particularly maddening problem I hope you won't encounter, but which you will when viewing your build file, is that it often seems **not to update** all of your work. For example, you may modify your menu order or the contents of a file, but when you update your build file and click on certain menu items, the changes are not displayed.

The reason for this is a rather quirky, but logical, behavior. The build file displays the most updated pages **only** for files or folders that you have modified. Therefore, if you modify some files and not others, and click items corresponding to files you didn't modify, the "older version" is displayed for those pages.

In other words, a different build file version is created for every change you make, which you can verify by sorting your files by timestamp. Build files with older timestamps will display a page corresponding to the changes made at that time. If you want to show the most current build files you have to open every page, save it, close it, and update your build file. Note that you only need to do this to see the most current pages in your build files. This behavior does not occur on your live pages when you commit and/or push your changes to live pages, whether on public or private branches.