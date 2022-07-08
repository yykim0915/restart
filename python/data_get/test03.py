from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import datetime
from dateutil.relativedelta import relativedelta
import urllib
import requests
import pandas as pd
import xmltodict
import json

before_day = (datetime.date.today() - datetime.timedelta(days=10)).strftime('%Y%m%d')
#before_day = (datetime.date.today() - relativedelta(years=1)).strftime('%Y%m%d')
today = datetime.date.today().strftime('%Y%m%d')

key='ytO8MzCAxdTXu0V%2BMZcyr4LxBAGSN7mp5LwqjOb%2F3JehCvI3QB8nGO%2FUETs2Q1JsMCkdM587ybjQo%2FdaDCrvzA%3D%3D'
url = f'http://api.data.go.kr/openapi/tn_pubr_public_city_tour_api?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1,
                          quote_plus('numOfRows') : 10,
                          quote_plus('startCreateDt') : before_day,
                          quote_plus('endCreateDt') : today})
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)

citytour=data['response']['body']['items']['item']
#추가하고 싶은 리스트 생성
ctprvnNm=[]
signguNm=[]
cityTourCourse=[]
brdngPlaceNm=[]
courseInfo=[]

for i in citytour:
    ctprvnNm.append(i['ctprvnNmCT'])
    signguNm.append(i['signguNmCT'])
    cityTourCourse.append(i['cityTourCourseCT'])
    brdngPlaceNm.append(i['brdngPlaceNmCT'])
    courseInfo.append(i['courseInfoCT'])

df=pd.DataFrame([state_dt,decide_cnt,death_cnt,acc_exam_cnt]).T
df.columns=['시도명','시군구명','시티투어코스명','시티투어탑승장소명','시티투어코스정보']
df=df.sort_values(by='기준일', ascending=True)

# csv 파일 생성
df.to_csv('citytour.csv')
# 메모장
df.to_csv('citytour.txt')
