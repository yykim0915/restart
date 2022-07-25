const express = require('express')
const bodyParser = require('body-parser')
const dfd = require('dataframe-js')

//mongodbCompass
from pymongo import MongoClient
client = MongoClient("mongodb://3.38.64.25:27017")
db = client['Tourweather']

// for d in db['tourweatherinfo'].find():
//     print(d['COURSE_ID'], d['courseAreaId'], d['sky'])

const app = express()
console.log('restful ===========================> ');

app.get("/Hello", (req, res)=> {
  res.send("Hello World")
})


//weather정보
app.get("/weather", (req, res) => {
  let df = new dfd.DataFrame(users);
  result = df.toJSON(users)
  df.show();
  res.writeHead(200)
  var template = `
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    </head>
    <body>
      ${result[i]['COURSE_ID']}
    </body>
    </html>
  `;
  res.end(template)
})


module.exports = app;
