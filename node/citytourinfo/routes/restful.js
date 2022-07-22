const express = require('express')
const bodyParser = require('body-parser')
const dfd = require('dataframe-js')

//mongodbCompass
from pymongo import MongoClient
client = MongoClient("mongodb://3.38.64.25:27017")
db = client['st_db']

// for d in db['accom_tb'].find():
//     print(d['sg_cd'], d['ac_name'])



const app = express()
console.log('restful ===========================> ');

app.get("/Hello", (req, res)=> {
  res.send("Hello World")
})


//-- 시티투어 상세정보 정보 검색 ----------------
app.get('/citytourinfo', function(req, res ) {
  var qStr = '';
  //console.log('---------req.query.sg_cd --> ', req.query.sg_cd);


  if(req.query.sg_cd != null) {
    qStr = 'select a.ct_cd , ct_name, a.sg_cd, ct_charge, ct_oper, ct_phone , ct_img, cs_no, cs_name from citytour_tb a, course_tb b where a.ct_cd = b.ct_cd and a.sg_cd = '+ req.query.sg_cd;
    qStr += " order by a.ct_cd, cs_no asc"
    //console.log('sql --> ', qStr);

    let result = pool.query(qStr);

    res.writeHead(200);
    var template = `
        <!doctype html>
        <html>
        <head>
          <meta charset="utf-8">
          <title>시티투어 정보</title>
        <style>
        body {
        	width: 230px;
        	height: 335x;
        }
        td {
        	font-family: 'Inter';
        	font-style: normal;
        	font-weight: 700;
        	font-size: 13px;
        	line-height: 16px;
        	align-items: center;
        	color: #7C7C7C;

        }
        </style>
        </head>
        <body>
        <table border="0" width="100%" >
        <tbody>
        `;

      if ( result.length > 0  ) {
        ct_cd_str = ""
        course_temp = ""

        for (var i=0; i<result.length ; i++) {
          if ( ct_cd_str != result[i]['ct_cd'] ) {
            if ( ct_cd_str != "" ) {
              template += course_temp + '<p></td></tr>';
              course_temp = ""
            }
            template += `
               <tr>
                 <td style="padding-left: 10px" >* ${result[i]['ct_name']}<br>tel: ${result[i]['ct_phone']}
                 </td>
               </tr>
               <tr>
                 <td style="text-align: center"><img src="img/route.png" width="172" height="51" alt=""/></td>
               </tr>
               <tr>
                 <td style="text-align: center">
            `;
            ct_div = true;
              //<td width="75" style="text-align: right"><img src="${result[i]['ct_img']}" width="50" height="50" alt=""/></td>
          } else {
            ct_div = false;
          }

          //-- 전체 코스 이미지 있으면, 출력 -> 없으면, 코스명 전체 출력
          if ( ct_div && result[i]['ct_img'] != "" ) {
            course_temp += `
                  <img src="./img/city_course/${result[i]['ct_img']}" width="100%" alt=""/>
                `;
          }

          if ( result[i]['ct_img'] == "" ) {
            if ( !ct_div ){
              course_temp += " - ";
            }
            course_temp += result[i]['cs_name'];
          }

          ct_cd_str = result[i]['ct_cd'];
        }

        template += course_temp + '<p></td></tr>';

      } else {
        console.log('no data ==============','\n');
        template += `
          <tr>
          <td >검색결과 없음</td>
          </tr>
          `;
      }

      template += `
          </tbody>
          </table>
          </body>
          </html>
          `;
      res.end(template);
    } else {
      console.log('no data ==============','\n')

    }

});



//-- 시군 selectbox  ----------------
app.get('/sigun', function(req, res ) {
  var qStr = 'SELECT * FROM sigun_tb order by sg_nm asc ';

  console.log('sql --> ', qStr);
  let result = pool.query(qStr);

  res.writeHead(200);
  var template = `<select class ="local" name="local" id="local">`;

  if ( result.length >0  ) {
    for (var i=0; i<result.length ; i++){
      template += ` <option value=${result[i]['sg_cd']}>${result[i]['sg_nm']}</option> `;
    }
  }
  template += ` </select>`;
  res.end(template);

});


module.exports = app;
