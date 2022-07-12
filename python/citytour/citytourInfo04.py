#mongDB Compass에서 파일(csv,xlsx) 연결하기
#pip install pymongo

from pymongo import MongoClient

client = MongoClient("mongodb://13.125.166.42:27017/")
db = client['test'] #mongDB Compass-test에 접속
#print(client.list_database_names())
#[READ_ME_TO_REOVER_YOUR_DATA ~ ~]


#test(db)-citytourinfo(collection) 데이터 입력하기
# data = {
#     'SIGUN_CD' : '경기도'
#     'SIGUN_NM' : '가평군'
#     'CITYTOUR_COURSE' : '가평시티투어'
#     'CITYTOUR_COURSE_INFO' : '가평터미널'
#     'addr' : '경기 가평군 가평읍 가화로 51'
#     'latitude' : '37.8245457'
#     'longitude' : '127.5154443'
# }
# dpInsert = db.citytourinfo.insert_one(data)


#test(db)-citytourinfo(collection) 데이터 출력하기
for d in db['citytourinfo'].find():
     print(d['SIGUN_CD'], d['SIGUN_NM']), d['CITYTOUR_COURSE'], d['CITYTOUR_COURSE_INFO'], d['addr'], d['latitude'], d['longitude']
