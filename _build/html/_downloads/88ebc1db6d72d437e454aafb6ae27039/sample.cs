        public void Test()
        {
            var connection = OpenConnection("192.168.4.62", 5000, "sqream", "sqream", "master");

            ExecuteSQLCommand(connection, "create or replace table tbl_example as select 1 as x , 'a' as y;");

            var tableData = ReadExampleData(connection, "select * from tbl_example;");
        }

        /// <summary>
        /// Builds a connection string to sqream server and opens a connection
        /// </summary>
        /// <param name="ipAddress">host to connect</param>
        /// <param name="port">port sqreamd is running on</param>
        /// <param name="username">role username</param>
        /// <param name="password">role password</param>
        /// <param name="databaseName">database name</param>
        /// <param name="isCluster">optional - set to true when the ip,port endpoint is a server picker process</param>
        /// <returns>
        /// SQream connection object
        /// Throws SqreamException if fails to open a connction
        /// </returns>
        public SqreamConnection OpenConnection(string ipAddress, int port, string username, string password, string databaseName, bool isCluster = false)
        {
            // create the connection string according to the format
            var connectionString = string.Format(
                "Data Source={0},{1};User={2};Password={3};Initial Catalog={4};Cluster={5}",
                ipAddress,
                port,
                username,
                password,
                databaseName,
                isCluster
                );

            // create a sqeram connection object
            var connection = new SqreamConnection(connectionString);

            // open a connection
            connection.Open();

            // returns the connection object
            return connection;
        }

        /// <summary>
        /// Executes a SQL command to sqream server
        /// </summary>
        /// <param name="connection">connection to sqream server</param>
        /// <param name="sql">sql command</param>
        /// <exception cref="InvalidOperationException"> thrown when the connection is not open</exception>
        public void ExecuteSQLCommand(SqreamConnection connection, string sql)
        {
            // validates the connection is open and throws exception if not
            if (connection.State != System.Data.ConnectionState.Open)
                throw new InvalidOperationException(string.Format("connection to sqream is not open. connection.State: {0}", connection.State));

            // creates a new command object utilizing the sql and the connection
            var command = new SqreamCommand(sql, connection);

            // executes the command
            command.ExecuteNonQuery();
        }

        /// <summary>
        /// Executes a SQL command to sqream server, and reads the result set usiing DataReader
        /// </summary>
        /// <param name="connection">connection to sqream server</param>
        /// <param name="sql">sql command</param>
        /// <exception cref="InvalidOperationException"> thrown when the connection is not open</exception>
        public List<Tuple<int, string>> ReadExampleData(SqreamConnection connection, string sql)
        {
            // validates the connection is open and throws exception if not
            if (connection.State != System.Data.ConnectionState.Open)
                throw new InvalidOperationException(string.Format("connection to sqream is not open. connection.State: {0}", connection.State));

            // creates a new command object utilizing the sql and the connection
            var command = new SqreamCommand(sql, connection);

            // creates a reader object to iterate over the result set
            var reader = (SqreamDataReader)command.ExecuteReader();

            // list of results
            var result = new List<Tuple<int, string>>();

            //iterate the reader and read the table int,string values into a result tuple object
            while (reader.Read())
                result.Add(new Tuple<int, string>(reader.GetInt32(0), reader.GetString(1)));

            // return the result set
            return result;
        }

