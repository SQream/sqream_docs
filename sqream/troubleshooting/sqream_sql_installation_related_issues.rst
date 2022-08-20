.. _sqream_sql_installation_related_issues:

***********************
SQream SQL Installation Related Issues
***********************

The **SQream SQL Installation Related Issues** page describes how to resolve SQream SQL installation related issues.

Upon running sqream sql for the first time, you may get an error ``error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory``.

Solving this error requires installing the ncruses or libtinfo libraries, depending on your operating system.

* Ubuntu:

   #. Install ``libtinfo``:
      
      ``$ sudo apt-get install -y libtinfo``
   #. Depending on your Ubuntu version, you may need to create a symbolic link to the newer libtinfo that was installed.
   
      For example, if ``libtinfo`` was installed as ``/lib/x86_64-linux-gnu/libtinfo.so.6.2``:
      
      ``$ sudo ln -s /lib/x86_64-linux-gnu/libtinfo.so.6.2 /lib/x86_64-linux-gnu/libtinfo.so.5``
      
* CentOS / RHEL:

   #. Install ``ncurses``:
   
      ``$ sudo yum install -y ncurses-libs``
   #. Depending on your RHEL version, you may need to create a symbolic link to the newer libtinfo that was installed.
   
      For example, if ``libtinfo`` was installed as ``/usr/lib64/libtinfo.so.6``:
      
      ``$ sudo ln -s /usr/lib64/libtinfo.so.6 /usr/lib64/libtinfo.so.5``