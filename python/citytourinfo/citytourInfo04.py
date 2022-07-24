from pymongo import MongoClient
import pandas as pd
import numpy as np
import os
import webbrowser
import folium

#python - mongDB Compass 연결하기
#pip install pymongo
client = MongoClient("mongodb://3.38.64.25:27017")
db = client['test'] #DBname-test에 접속
#print(client.list_database_names())
#['READ__ME_TO_RECOVER_YOUR_DATA', 'admin', 'config', 'test']
sql = "select SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude from citytourinfo"


#test(db)-citytourinfo(collection) 데이터 입력하기
# data = {
#     'SIGUN_CD' : '경기도',
#     'SIGUN_NM' : '가평군',
#     'CITYTOUR_COURSE' : '가평시티투어',
#     'CITYTOUR_COURSE_INFO' : '가평터미널',
#     'addr' : '경기 가평군 가평읍 가화로 51',
#     'latitude' : '37.8245457',
#     'longitude' : '127.5154443'
# }
# dpInsert = db.citytourinfo.insert_one(data)
#     {
#     'SIGUN_CD' : '경기도',
#     'SIGUN_NM' : '가평군',
#     'CITYTOUR_COURSE' : '가평시티투어',
#     'CITYTOUR_COURSE_INFO' : '가평레일바이크',
#     'addr' : '경기 가평군 가평읍 장터길 14',
#     'latitude' : '37.8293425',
#     'longitude' : '127.5154088'
# }



#test(db)-citytourinfo(collection) 데이터 출력하기
# for d in db['citytourinfo'].find():
    # print(d['SIGUN_CD'], d['SIGUN_NM'], d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude'])
    #print(db.citytourinfo.find_one({'CITYTOUR_COURSE':'가평시티투어'})['text']) #1행 출력


#map에 필요한 column만 저장
# df_mapsample = df[['CITYTOUR_COURSE','CITYTOUR_COURSE_INFO','latitude','longitude']]
# print(df_mapsample)

#map에 필요한 column만 저장
# for d in db['citytourinfo'].find():
#     print(d['CITYTOUR_COURSE'], d['latitude'], d['longitude'])
# data = ['CITYTOUR_COURSE', 'latitude', 'longitude']
# latitude = 37.8245457
# longitude = 127.5154443

latitude = 37.8245457
longitude = 127.5154443

#map marker
def citytourinfo_map(default_location=[latitude, longitude], default_zoom_start=20):
    map_osm = folium.Map(location=[latitude, longitude], zoom_start=12)

    for d in db['citytourinfo'].find():
        print(d['CITYTOUR_COURSE'], d['latitude'], d['longitude'])
    data = ['CITYTOUR_COURSE', 'latitude', 'longitude']

    #itertuples - tuple을 반복하는 객체 반환
    for row in df.itertuples():
        CITYTOUR_COURSE, latitude, longitude = row[1:]
        if CITYTOUR_COURSE == '가평시티투어':
            icon = Icon(color = 'red', icon = 'info-sign')
        elif CITYTOUR_COURSE == '여주시티투어':
            icon = Icon(color = 'blue', icon = 'info-sign')
        elif CITYTOUR_COURSE == '파주시티투어':
            icon = Icon(color = 'yellow', icon = 'info-sign')
        else:
            break

    for row in df.itertuples():
        CITYTOUR_COURSE, latitude, longitude = row[1:]
        print(row)

    folium.Marker([latitude, longitude],
                  icon=folium.Icon(color='red', icon='star'),
                  popup='<iframe width="500" height="300" src="https://www.daum.net/" title="daum사이트" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                  tooltip='big data').add_to(map_osm)
    map_osm.save('./data/map_citytourInfo04.html')
    webbrowser.open('file://'+ os.path.realpath('./data/map_citytourInfo04.html'))

print('map save')
citytourinfo_map()
