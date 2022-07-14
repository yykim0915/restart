var express = require("express");
var mysql = require("mysql");
var connection = mysql.createConnection({
  host : 'database-1.crostskxzxwu.ap-northeast-2.rds.amazonaws.com',
  user : 'admin',
  password : 'admin1234',
  database : 'st_db'

  // host : 13.125.166.42:3306,
  // user : 'admin',
  // password : '1234',
  // database : 'test'
})

var app = express();

connection.connect(function(err) {
  if(!err) {
    console.log("Database is connected...\n\n");
  } else {
    console.log("Error connectiong database...\n\n");
  }
});

app.get('/', function(req, res) {
  connection.query('select * from test', function(err, rows, fields) {
    connection.end();
    if(!err) {
      res.send(rows);
      console.log('The solution is : ', rows);
    } else {
      console.log('Error while perfoming Query ');
    }
  })
})

app.listen(8080, function () {
  console.log('8080 Port : Server started...');
})
