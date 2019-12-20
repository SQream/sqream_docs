#!/usr/bin/env python
import pysqream as sq

# Print version
print (sq.version_info())

# Get a connector
connection = sq.Connector()
# Connect to your SQream DB instance
connection.connect('<sqream db hostname>',<sqream db port>,'<database name>','<username>','<password>',False,60)

try: 
  # Prepare and execute a statement
  connection.prepare('SELECT show_version()')
  connection.execute()
  print(connection.fetch_all_as_dict())
finally:
  # Close statement
  connection.close()

# Close off the connection
connection.close_connection()