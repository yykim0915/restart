from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import datetime
from dateutil.relativedelta import relativedelta
import urllib
import requests
import pandas as pd
import xmltodict
import json


#https://data.gg.go.kr(경기데이터드림)-시티투어정보현황(개방표준)
key='2a3b8662c28f474883d6d78ce9da3f28'
url = f'https://openapi.gg.go.kr/Citytourinfostus?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1,
                          quote_plus('numOfRows') : 10,
                          quote_plus('SIGUN_CD') : 4182000000,     #시군코드:가평군(4182000000)
                          quote_plus('SIGUN_NM') : 4182003001})   #시군명
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)

citytour=data['response']['body']['items']['item']
#추가하고 싶은 리스트 생성
SIDO_NM=[]
SIGNGU_NM=[]
CITYTOUR_COURSE_NM=[]
CITYTOUR_BRDNG_PLC_INFO=[]
CITYTOUR_COURSE_INFO=[]

for i in citytour:
    SIDO_NM.append(i['SIDO_NM'])
    SIGNGU_NM.append(i['SIGNGU_NM'])
    CITYTOUR_COURSE_NM.append(i['CITYTOUR_COURSE_NM'])
    CITYTOUR_BRDNG_PLC_INFO.append(i['CITYTOUR_BRDNG_PLC_INFO'])
    CITYTOUR_COURSE_INFO.append(i['CITYTOUR_COURSE_INFO'])

df=pd.DataFrame([SIDO_NM,SIGNGU_NM,CITYTOUR_COURSE_NM,CITYTOUR_BRDNG_PLC_INFO,CITYTOUR_COURSE_INFO]).T
df.columns=['시도명','시군구명','시티투어코스명','시티투어탑승장소명','시티투어코스정보']
df=df.sort_values(by='기준일', ascending=True)


df.to_csv('./data/Citytourinfostus.csv') # csv 파일생성
df.to_csv('./data/Citytourinfostus.txt') # txt 파일생성
