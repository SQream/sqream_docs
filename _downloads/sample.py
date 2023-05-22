import pysqream_blue

# Create a connection object
con = pysqream_blue.connect(host='blue_cluster.isqream.com', port=443, database='master', access_token='#########################')

# Create a new cursor
cur = con.cursor() 
# The select statement - in this example a CPU based query to list the defined databases in the Blue cluster
statement = 'SELECT * FROM nba'
# Execute statement 
cur.execute(statement)
res = cur.fetchall()
#Print results
print(res)
#Close the connection
con.close()