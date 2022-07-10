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
                          quote_plus('SIGUN_CD'),    #경기도
                          quote_plus('SIGUN_NM'))    #가평군
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)
