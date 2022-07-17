const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const request = require('request');
const moment = require('moment');
const dateutil = require('date-utils');
const mongoClient = require('mongodb').MongoClient


var keys='ytO8MzCAxdTXu0V%2BMZcyr4LxBAGSN7mp5LwqjOb%2F3JehCvI3QB8nGO%2FUETs2Q1JsMCkdM587ybjQo%2FdaDCrvzA%3D%3D'
var url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnVilageFcst';
var queryParams = '?' + encodeURIComponent('serviceKey') + '=' + keys; /*Service Key*/
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /* */
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('10'); /* */
queryParams += '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('JSON'); /* */
queryParams += '&' + encodeURIComponent('CURRENT_DATE') + '=' + encodeURIComponent('2022070110'); /* */
queryParams += '&' + encodeURIComponent('HOUR') + '=' + encodeURIComponent('24'); /*예보기간(24)*/
queryParams += '&' + encodeURIComponent('COURSE_ID') + '=' + encodeURIComponent('55'); /*코스ID(1)*/


//define scheme
var dataSchema = mongoose.Schema({
      courseAreaId : Varchart
      courseAreaName : Varchart
      maxTa : Number
      minTa : Number
      sky : Number
      pop : Number
});

var Tourweather = mongoose.model('tourweatherinfo',dataSchema);

// getdata
router.get('/getdata', function(req, res, next) {
  request({
      url: url + queryParams,
      method: 'GET'
  }, function (error, response, body) {
      //console.log('Status', response.statusCode);
      //console.log('Headers', JSON.stringify(response.headers));
      //console.log('Reponse received', body);

      Tourweather.find({}).remove().exec();

      let data = JSON.parse(body);
      res.json(data);

      for(i in data['response']['body']['items']['item']) {
        courseAreaId_v  = data['response']['body']['items']['item'];
        courseAreaName_v  = data['response']['body']['items']['item'];
        maxTa_v  = data['response']['body']['items']['item'];
        sky_v = data['response']['body']['items']['item'];
        pop_v = data['response']['body']['items']['item'];

        var newWeather = new Tourweather({courseAreaId : courseAreaId_v, courseAreaName : courseAreaName_v, maxTa : maxTa_v, sky : sky_v, pop : pop_v});
        newWeather.save(function(err, result) {
          if (err) return console.error(err);
          console.log(new Date(),result);
        })
      }
  });
});

// list
router.get('/list', function(req, res, next) {
      Tourweather.find({},function(err,docs){
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
        Tourweather.findOne({},function(err,docs){
          if(err) console.log('err');
          res.send(docs);
        });
      } else {
        Tourweather.find({'COURSE_ID':input},function(err,docs){
          if(err) console.log('err');
          res.send(docs);
        });
      }
});

module.exports = router;

Tourweather.find({}).exec(function(err,weathers){
      console.log("Query 1");
      console.log(new Date(), weathers+"\n");
      return;
});
