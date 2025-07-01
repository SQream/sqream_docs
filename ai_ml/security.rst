{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _security:\
\
\
Security Requirements\
=====================\
\
AISQream allows creating and executing Python modules within the database engine. Due to the nature of executing external code, there are strict security and permission requirements in place.\
\
Python Module Permissions\
-------------------------\
\
Only users with `SUPERUSER` privileges can:\
\
- Create or replace Python modules using `CREATE MODULE`\
- Register new Python-based algorithms with `REGISTER ALGORITHM`\
\
Granting Execution Permissions\
------------------------------\
\
A SUPERUSER can grant execution rights on specific modules to other users or roles using:\
\
.. code-block:: sql\
\
   GRANT EXECUTE ON MODULE module_name TO role;\
\
This allows regular (non-superuser) roles to run predefined module functions, without being able to modify or register new ones.\
\
Security Notes\
--------------\
\
- Python code executes with default Linux privileges on the worker machine\
- Malicious or careless code (e.g. infinite loops, system calls) may impact stability\
- Users should be careful when including file paths, shell access, or loading external libraries\
\
Module Creation Example:\
\
.. code-block:: sql\
\
   CREATE OR REPLACE MODULE safe_module OPTIONS (\
       path = '/secure/path/myfuncs.py',\
       entry_points = [\
           [ name = 'safe_sum',\
             param_types = [INT, INT],\
             return_type = INT,\
             gpu_acceleration = TRUE ]\
       ]\
   );\
\
   GRANT EXECUTE ON MODULE safe_module TO analyst_role;\
\
Recommendations\
---------------\
\
- Only trusted users should be granted module creation privileges\
- Maintain audit logs of module definitions\
- Validate all Python code before deployment\
- Monitor memory usage and CPU time of module execution\
}