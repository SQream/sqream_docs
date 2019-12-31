const Connection  = require('sqreamdb');
const config  =  {
  host: '<host>',
  port: <port>,
  username: '<username>',
  password: '<password>',
  connectDatabase: '<database>',
  cluster: '<true | false>',
  ssl: '<true | false>',
  service: '<workload manager service>'  
  };
  
const query1  =  'SELECT 1 AS test, 2*6 AS "dozen"';

const myConnection  = new Connection(config);
myConnection.runQuery(query1, function  (err, data){
   console.log(err, data);  
});