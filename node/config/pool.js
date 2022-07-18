/* 이 파일 있는 곳 또는 상위 폴더에서 아래 처럼 실행 필요

npm install sync-mysql

*/
var mysql = require('sync-mysql');
var connection = new mysql({
  host : 'database-1.csutjqozrvur.us-west-1.rds.amazonaws.com',
  user : 'admin',
  password : 'admin1234',
  database : 'st_db'
});
//--------------------------------

module.exports = connection;
