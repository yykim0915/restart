import requests
import json
import math
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
#from config  import *
#import matplotlib.pyplot as plt

#------------------------
# 접속 get_request_url( )
# 데이터처리 main()
# csv저장함수 make_file()
#------------------------
#https://data.gg.go.kr(경기데이터드림)-시티투어정보현황(개방표준)


result = []

def get_totalCount_fromUrl():
    url='https://openapi.gg.go.kr/Citytourinfostus'
    parameter =  '?ServiceKey='+ serviceKey
    parameter += '&pageNo=1'
    parameter += '&numOfRows=10'
    url += parameter
    res = requests.get(url)

    if res.status_code == 200 :
        root = ET.fromstring(res.text)
        #totalCount = int(root.find('body').find('totalCount').text)
        totalCount = int(root.find('response').find('body').find('items').text)
        return totalCount
    else:
        print(url, '접속실패')
        return None


def get_request_url(pageNo, numOfRows):
    url='https://openapi.gg.go.kr/Citytourinfostus'
    parameter =  '?serviceKey='+ serviceKey
    parameter += '&pageNo=' + str(pageNo)
    parameter += '&numOfRows=' + str(numOfRows)
    url = url  + parameter

    res = requests.get(url)
    if res.status_code == 200 :
        return res.text
    else:
        print(url, '접속실패')


def make_file(fileData, fileType):
    if fileType == 'TXT':
        print(fileData)
        file = open('./data/citytourInfo02.txt','w',encoding='UTF-8')
        file.write(str(fileData))
        file.close()
        print('filesave')
        print()

    elif fileType == 'CSV':
        dataFrame = pd.DataFrame(fileData)
        dataFrame.to_csv('./data/citytourInfo02.csv' , encoding='utf-8', mode='w')
        print('filesave')
        print()

    elif fileType == 'XLSX':
        dataFrame = pd.DataFrame(fileData)
        dataFrame.to_excel('./data/citytourInfo02.xlsx',sheet_name='mysheet')
        print('filesave')
        print()

    elif fileType == 'JSON':
        dataFrame = pd.DataFrame(fileData)
        result = dataFrame.to_json(orient="split")
        parsed = json.loads(result)
        file = open('./data/citytourInfo02.json','w',encoding='UTF-8')
        file.write(json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False))
        file.close()
        print('filesave')
        print()


def main():
    parsedData = pd.DataFrame()
    nEndPage = 1
    pageNo = 1
    numOfRows = 10

    totalCount = get_totalCount_fromUrl()
    print('totalCount =',totalCount )
    nEndPage = math.ceil(totalCount/numOfRows)
    print('nEndPage =',nEndPage )

    for pageNo in range(1, nEndPage+1):
        rawData = get_request_url(pageNo, numOfRows)
        result = pd.read_xml(rawData, xpath='.//item')
        parsedData = pd.concat([parsedData, result])

    make_file(parsedData, 'TXT')
    make_file(parsedData, 'CSV')
    make_file(parsedData, 'XLSX')
    make_file(parsedData, 'JSON')

#if __name__ == '__main__':
main()
