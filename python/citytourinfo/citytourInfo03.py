import urllib.request
import datetime
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import folium
import os
import webbrowser
from pymongo import MongoClient

client = MongoClient("mongodb://3.38.64.25:27017")
db = client['test'] #DBname(test)에 접속
sql = "select SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude from citytourinfo"

#--------------------
# fname = '/data/mongo/citytourinfo.csv'
# score = pd.read_csv(fname, encoding = 'cp949')
# print(score)
#print(score.head(2))  #row 1,2행 출력
#--------------------


#test(db)-citytourinfo(collection) 데이터 출력하기
# for d in db['citytourinfo'].find():
    # print(d['SIGUN_CD'], d['SIGUN_NM'], d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude'])
#print(db.citytourinfo.find_one({'CITYTOUR_COURSE':'가평시티투어'})['text']) #1행 출력


#--------------------
#map에 필요한 column만 저장
# df_mapsample = df['CITYTOUR_COURSE','CITYTOUR_COURSE_INFO','latitude','longitude']
#     print(df_mapsample)
#--------------------


#map 시각화하기(zoom값은 0~20까지)
def citytourinfo_map(default_location=[35.53898, 129.31125], default_zoom_start=20):
    base_map = folium.Map(location=darault_location, control_scale=True, zoom_start=default_zoom_start)

    #itertuples - tuple을 반복하는 객체 반환
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

    #map Marker 클릭시 popup
    Marker(location=[latitude,longitude], popup=f'시티투어코스정보 : {CITYTOUR_COURSE_INFO}', icon = icon).add_to(base_map)
    base_map.save('./data/map_citytourInfo03.html')
    return base_map

print('citytourinfo 맵')
citytourinfo_map()
