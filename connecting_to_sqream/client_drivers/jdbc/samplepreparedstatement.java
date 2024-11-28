try (BufferedReader br = new BufferedReader(new FileReader(csv_file))) {

            int i = 0;
            String csv_line;
            int batchSize = 1000000;
            String url = "jdbc:Sqream://" + host + ":" + port +
                "/riru;cluster=false;user=sqream;password=sqream";
            LocalDateTime start_time = LocalDateTime.now();

            Class.forName("com.sqream.jdbc.SQDriver");

            Connection con =
                DriverManager.getConnection(url, "sqream", "sqream");

            String inStmt =
                "INSERT INTO message values(?,?,?,?,?,?,?,?,?,?,?,?)";

            PreparedStatement ps = con.prepareStatement(inStmt);

            while((csv_line = br.readLine()) != null){
                String[] message = csv_line.split(",");

                ps.setString(1, message[0].trim());
                ps.setInt(2, Integer.parseInt(message[1].trim()));
                ps.setInt(3, Integer.parseInt(message[2].trim()));
                ps.setInt(4, Integer.parseInt(message[3].trim()));
                ps.setInt(5, Integer.parseInt(message[4].trim()));
                ps.setString(6, message[5].trim());
                ps.setString(7, message[6].trim());
                ps.setString(8, message[7].trim());
                ps.setString(9, message[8].trim());
                ps.setString(10, message[9].trim());
                ps.setInt(11, Integer.parseInt(message[10].trim()));
                ps.setInt(12, Integer.parseInt(message[11].trim()));

                ps.addBatch();

                if(++i == batchSize) {
                    i = 0;
                    ps.executeBatch();
                    ps.close();
                    System.out.println(LocalDateTime.now().toString() +
                                       ": Inserted " + batchSize + " records.");
                    ps = con.prepareStatement(inStmt);
                }


            }