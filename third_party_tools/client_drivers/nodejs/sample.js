const Connection = require('@sqream/sqreamdb');

const config  =  {
  host: 'localhost',
  port: 3109,
  username: 'rhendricks',
  password: 'super_secret_password',
  connectDatabase: 'raviga',
  cluster: true,
  is_ssl: true,
  service: 'sqream'  
  };
  
const query1  =  'SELECT 1 AS test, 2*6 AS "dozen"';

const sqream = new Connection(config);
sqream.execute(query1).then((data) => {
   console.log(data);
}, (err) => {
   console.error(err);
});