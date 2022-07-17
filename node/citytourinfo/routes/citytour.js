const express = require('express')
const bodyParser = require('body-parser')
const dfd = require('dataframe-js')

//mongodbCompass
// from pymongo import MongoClient
// client = MongoClient("mongodb://3.38.64.25:27017")
// db = client['test']

// for d in db['citytourinfo'].find():
//     print(d['SIGUN_CD'], d['SIGUN_NM']), d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude']
//mongodbCompass


const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended : false }))
app.use(express.json())
app.use(express.urlencoded({ extended : true }))

const users = [
  { id: 1, name : "user1" },
  { id: 2, name : "user2" },
  { id: 3, name : "user3" },
]

app.get("/Hello", (req, res)=> {
  res.send("Hello World")
})


//citytourinfo Marker
app.get("/api/citytour", (req, res) => {
fname = '/data/mongo/citytourinfo.csv'
score = pd.read_csv(fname, encoding = 'cp949')
print(score)

def citytourinfo_map(default_location=[35.53898, 129.31125], default_zoom_start=20):
    base_map = folium.Map(location=darault_location, control_scale=True, zoom_start=default_zoom_start)

  //itertuples - tuple을 반복하는 객체 반환
  for row in df.itertuples():
      SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude = row[1:]
      if CITYTOUR_COURSE == '가평시티투어':
          icon = Icon(color = 'red', icon = 'info-sign')
      elif CITYTOUR_COURSE == '여주시티투어':
          icon = Icon(color = 'blue', icon = 'info-sign')
      elif CITYTOUR_COURSE == '파주시티투어':
          icon = Icon(color = 'yellow', icon = 'info-sign')
      else:
          break

  for row in df.itertuples():
      SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude = row[1:]
      print(row)

  Marker(location=[latitude,longitude],
      popup=f'시티투어코스정보 : {CITYTOUR_COURSE_INFO}', icon = icon).add_to(base_map)
  base_map.save('map_citytourinfo.html')
  #return base_map

print('citytourinfo 맵')
citytourinfo_map()
})
//citytourinfo Marker




app.get("/api/users", (req, res) => {
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
      ${result}
    </body>
    </html>
  `;
  res.end(template)
})

module.exports = app;
