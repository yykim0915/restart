# from bottle import route, run
from bottle import route, run, error, static_file, template, request, response, view
import pymysql
import pandas as pd
import folium
import base64
import json
import requests

#mongodbCompass
# from pymongo import MongoClient
# client = MongoClient("mongodb://3.38.64.25:27017")
# db = client['test']
#db = client['st_db']

# for d in db['accom_tb'].find():
    # print(d['sg_cd'], d['ac_name'])

#-------------------------------
#-------------------------------
fname = '/data/mongo/citytourinfo.csv'
df = pd.read_csv(fname, encoding = 'cp949')
print(df)

#map정보
@route('/map')
@route('/map/<CITYTOUR_COURSE>')
def index(CITYTOUR_COURSE='가평시티투어'):
    print('== map page start ========>')

    #map에 필요한 column만 변수에 저장
    df_sample = df[['CITYTOUR_COURSE', 'CITYTOUR_COURSE_INFO', 'latitude', 'longitude']]
    print(df_sample)

    #널값 제거 및 제거한 값을 새로운 변수에 저장
    df_drop_sample = df_sample.dropna(axis=0)

    #null값 제거한 값을 새로운 변수에 저장
    df_final = df_drop_sample
    print(df_final.isnull().sum())

    #map 시각화하기(zoom값은 0~20까지)
    def citytourinfo_map(default_location=[37.8245457, 127.5154443], default_zoom_start=8):
        base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)

        #itertuples - tuple을 반복하는 객체 반환
        for row in df_final.itertuples():
            CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, latitude, longitude = row[1:]
            if CITYTOUR_COURSE == '가평시티투어':
                icon = Icon(color = 'red', icon = 'info-sign')
            elif CITYTOUR_COURSE == '여주시티투어':
                icon = Icon(color = 'blue', icon = 'info-sign')
            elif CITYTOUR_COURSE == '파주시티투어':
                icon = Icon(color = 'green', icon = 'info-sign')
            else:
                break

            #map Marker 클릭시 popup
            Marker(location=[latitude,longitude], popup=f'정류장 이름 : {CITYTOUR_COURSE_INFO}', icon = icon).add_to(base_map)

        #map 저장하기
        base_map.save('map_citytourInfo03.html')
        return base_map

    #지도 출력하기
    print('map 저장')
    citytourinfo_map()

#-------------------------------
#-------------------------------
#weather정보
# @route('/weather')
# @route('/weather/<COURSE_ID>')
# def index(COURSE_ID='55'):
#     print('== weather page start ========>')
#
#     #weather정보 html생성
#     w_list = df.values.tolist()
#     citytour_page = '''
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8">
# </head>
# <body>
#      ${result[i]['COURSE_ID']}
# </body>
# </html>
# '''
# 	return citytour_page
#-------------------------------
#-------------------------------

run(host='0.0.0.0', port=8080, threaded=True)
