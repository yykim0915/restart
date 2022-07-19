import pandas as pd

#python - mongDB Compass 연결하기
#pip install pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://3.38.64.25:27017")
db = client['test'] #DBname(test)에 접속
#print(client.list_database_names())
#['READ__ME_TO_RECOVER_YOUR_DATA', 'admin', 'config', 'test']


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
#     {
#     'SIGUN_CD' : '경기도',
#     'SIGUN_NM' : '가평군',
#     'CITYTOUR_COURSE' : '가평시티투어',
#     'CITYTOUR_COURSE_INFO' : '가평레일바이크',
#     'addr' : '경기 가평군 가평읍 장터길 14',
#     'latitude' : '37.8293425',
#     'longitude' : '127.5154088'
# }
# dpInsert = db.citytourinfo.insert_one(data)


#test(db)-citytourinfo(collection) 데이터 출력하기
for d in db['citytourinfo'].find():
    print(d['SIGUN_CD'], d['SIGUN_NM'], d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude'])
#print(db.citytourinfo.find_one({'CITYTOUR_COURSE':'가평시티투어'})['text']) #1행 출력

#map에 필요한 column만 저장
df_mapsample = df[['CITYTOUR_COURSE','CITYTOUR_COURSE_INFO','latitude','longitude']]
print(df_mapsample)

#map에 필요한 column만 저장
# df=pd.DataFrame([SIGUN_CD,SIGUN_NM,CITYTOUR_COURSE,CITYTOUR_COURSE_INFO,addr,latitude,longitude])
# df.columns=['CITYTOUR_COURSE','CITYTOUR_COURSE_INFO','latitude','longitude']
# print(df)
