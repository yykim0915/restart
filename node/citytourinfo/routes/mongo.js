const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const request = require('request');
const moment = require('moment');
const dateutil = require('date-utils');
const mongoClient = require('mongodb').MongoClient


var keys='2a3b8662c28f474883d6d78ce9da3f28'
var url = 'https://openapi.gg.go.kr/Citytourinfostus';
var queryParams = '?' + encodeURIComponent('serviceKey') + '=' + keys; /* Service Key*/
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /* */
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('10'); /* */
queryParams += '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('JSON'); /* */
queryParams += '&' + encodeURIComponent('SIGUN_CD') + '=' + encodeURIComponent('41820'); /* */
queryParams += '&' + encodeURIComponent('SIGUN_NM') + '=' + encodeURIComponent(''); /* */


//define scheme
var dataSchema = mongoose.Schema({
      SIDO_NM : Number,
      SIGNGU_NM : Number,
      CITYTOUR_COURSE_NM : Number
});

var Citytour = mongoose.model('Citytourinfostus',dataSchema);

// getdata
router.get('/getdata', function(req, res, next) {
  request({
      url: url + queryParams,
      method: 'GET'
  }, function (error, response, body) {
      //console.log('Status', response.statusCode);
      //console.log('Headers', JSON.stringify(response.headers));
      //console.log('Reponse received', body);

      Citytour.find({}).remove().exec();

      let data = JSON.parse(body);
      res.json(data);

      for(i in data['response']['body']['items']['item']) {
        SIDO_NM_v  = data['response']['body']['items']['item'];
        SIGNGU_NM_v  = data['response']['body']['items']['item'];
        CITYTOUR_COURSE_NM_v  = data['response']['body']['items']['item'];

        var newWeather = new Citytour({SIDO_NM : SIDO_NM_v, SIGNGU_NM : SIGNGU_NM_v, CITYTOUR_COURSE_NM : CITYTOUR_COURSE_NM_v});
        newWeather.save(function(err, result) {
          if (err) return console.error(err);
          console.log(new Date(),result);
        })
      }
  });
});

// list
router.get('/list', function(req, res, next) {
      Citytour.find({},function(err,docs){
           if(err) console.log('err');
           res.writeHead(200);
           var template = `
           <!doctype html>
           <html>
           <head>
             <title>Result</title>
             <meta charset="utf-8">
           </head>
           <body>
             ${docs}
           </body>
           </html>
          `;
           res.end(template);
      });
});

// get
router.get('/get', function(req, res, next) {
      db = req.db;
      var input = req.query.input;
      if(input=='') {
        Citytour.findOne({},function(err,docs){
          if(err) console.log('err');
          res.send(docs);
        });
      } else {
        Citytour.find({'SIDO_NM':input},function(err,docs){
          if(err) console.log('err');
          res.send(docs);
        });
      }
});

module.exports = router;

Citytour.find({}).exec(function(err,weathers){
      console.log("Query 1");
      console.log(new Date(), weathers+"\n");
      return;
});
