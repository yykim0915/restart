from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import datetime
from dateutil.relativedelta import relativedelta
import urllib
import requests
import pandas as pd
import xmltodict
import json


#https://www.data.go.kr(공공데이터포털)-기상청_관광코스별 관광지 상세 날씨 조회서비스
key='ytO8MzCAxdTXu0V%2BMZcyr4LxBAGSN7mp5LwqjOb%2F3JehCvI3QB8nGO%2FUETs2Q1JsMCkdM587ybjQo%2FdaDCrvzA%3D%3D'
url = f'http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnVilageFcst?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1,
                          quote_plus('numOfRows') : 10,
                          quote_plus('dataType') : json,             #(XML/JSON)
                          quote_plus('CURRENT_DATE') : 2022070110,   #(2019122010)
                          quote_plus('HOUR') : 24,                   #예보기간(24)
                          quote_plus('COURSE_ID') : 55})              #코스ID(1)
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)

Tourweather=data['response']['body']['items']['item']
#추가하고 싶은 리스트 생성
courseAreaId=[]
courseAreaName=[]
maxTa=[]
minTa=[]
sky=[]
pop=[]

for i in Tourweather:
    courseAreaId.append(i['courseAreaId'])
    courseAreaName.append(i['courseAreaName'])
    maxTa.append(i['maxTa'])
    minTa.append(i['minTa'])
    sky.append(i['sky'])
    pop.append(i['pop'])

df=pd.DataFrame([courseAreaId,courseAreaName,maxTa,minTa,sky,pop]).T
df.columns=['코스-지역아이디','코스-지역이름','최고기온','최저기온','하늘상태','강수확률']
df=df.sort_values(by='코스-지역아이디', ascending=True)

df.to_csv('./data/TourStnInfoService.csv') # csv 파일생성
df.to_csv('./data/TourStnInfoService.txt') # txt 파일생성
