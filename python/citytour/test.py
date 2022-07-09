from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import datetime
from dateutil.relativedelta import relativedelta
import urllib
import requests
import pandas as pd
import xmltodict
import json

#before_day = (datetime.date.today() - datetime.timedelta(days=10)).strftime('%Y%m%d')
#before_day = (datetime.date.today() - relativedelta(years=1)).strftime('%Y%m%d')
#today = datetime.date.today().strftime('%Y%m%d')

key='ytO8MzCAxdTXu0V%2BMZcyr4LxBAGSN7mp5LwqjOb%2F3JehCvI3QB8nGO%2FUETs2Q1JsMCkdM587ybjQo%2FdaDCrvzA%3D%3D'
url = f'https://openapi.gg.go.kr/Citytourinfostus?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1,
                          quote_plus('numOfRows') : 10,
                          quote_plus('SIGUN_CD'),
                          quote_plus('SIGUN_NM'))
url2 = url + queryParams

response = urlopen(url2)
results = response.read().decode("utf-8")
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)
