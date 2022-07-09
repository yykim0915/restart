from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import datetime
from dateutil.relativedelta import relativedelta
import urllib
import requests
import pandas as pd
import xmltodict
import json


#https://www.data.go.kr(전국시티투어정보표준데이터)
key='ytO8MzCAxdTXu0V%2BMZcyr4LxBAGSN7mp5LwqjOb%2F3JehCvI3QB8nGO%2FUETs2Q1JsMCkdM587ybjQo%2FdaDCrvzA%3D%3D'
url = f'http://api.data.go.kr/openapi/tn_pubr_public_city_tour_api?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1,
                          quote_plus('numOfRows') : 10,
                          quote_plus('ctprvnNm'),  #시도명
                          quote_plus('signguNm'))  #시군구멩
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)
