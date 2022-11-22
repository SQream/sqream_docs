#!/usr/bin/env python

import pysqream

"""
Connection parameters include:
* IP/Hostname
* Port
* database name
* username
* password 
* Connect through load balancer, or direct to worker (Default: false - direct to worker)
* use SSL connection (default: false)
* Optional service queue (default: 'sqream')
"""

# Create a connection object

con = pysqream.connect(host='127.0.0.1', port=5000, database='master'
                   , username='sqream', password='sqream'
                   , clustered=False)

# Create a new cursor
cur = con.cursor()

# Prepare and execute a query
cur.execute('select show_version()')

result = cur.fetchall() # `fetchall` gets the entire data set

print (f"Version: {result[0][0]}")

# This should print the SQream DB version. For example ``Version: v2020.1``.

# Close cursor

cur.close()


# Finally, close the connection

con.close()