import pandas as pd
import folium
from folium import Marker, Icon, CircleMarker
from pymongo import MongoClient

client = MongoClient("mongodb://3.38.64.25:27017")
db = client['test'] #DBname(test)에 접속
sql = "select SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude from citytourinfo"

#test(db)-citytourinfo(collection) 데이터 출력하기
for d in db['citytourinfo'].find():
    print(d['SIGUN_CD'], d['SIGUN_NM'], d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude'])
#print(db.citytourinfo.find_one({'CITYTOUR_COURSE':'가평시티투어'})['text']) #1행 출력

#--------------------
# fname = '/data/mongo/citytourinfo.csv'
# df = pd.read_csv(fname, encoding = 'cp949')
# print(df)
# print(df.head(2))  #row 1,2행 출력
#--------------------
df = pd.DataFrame([SIGUN_CD, SIGUN_NM, CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, addr, latitude, longitude])
print(df)

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
    base_map.save('./data/map_citytourInfo03.html')
    return base_map

#지도 출력하기
print('map 저장')
citytourinfo_map()
