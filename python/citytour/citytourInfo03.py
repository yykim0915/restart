import time
import sys
import math
from config  import *
import urllib.request
import datetime
import json
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import folium  #map Markericon 띄우기
#from folium import Marker, Icon


fname='./data/citytour.csv'
score = pd.read_csv(fname, encoding='cp949')
print(score)
# print(score.head(2))

#map Markericon에 필요한 column만 저장
# df_mapsample = df['CITYTOUR_COURSE','CITYTOUR_COURSE_INFO','addr','x','y']
# print(df_mapsample.head(3)) #row 1,2,3행 출력
#display(df_mapsample.head(3))
# print()

#data null값 확인하기
# print('data null값 확인')
# display(df_mapsample.isnull().sum())

#data null값 제거 및 null값 제거한 값을 새로운 변수에 저장
#dropna(axis=0) null값 제거
# df_drop_sample = df_mapsample.dropna(axis=0)

#map visulzation
#zoom값은 0~20까지 가능
# def citytour_map(default_location=[35.53898, 129.31125], default_zoom_start=20):
#     base_map = folium.Map(location=darault_location,
#                             control_scale=True,
#                             zoom_start=default_zoom_start)

#설치된 그늘막 icon 생성하기
#itertuples() tuple을 반복하는 객체 반환
for row in df_final.itertuples():
    CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, x, y = row[1:]
    if CITYTOUR_COURSE_INFO ==‘가평순환버스’:
        icon = Icon(color='red', icon='info-sign')
    elif CITYTOUR_COURSE_INFO ==‘이천시티투어’:
        icon = Icon(color='blue', icon='info-sign')
    elif CITYTOUR_COURSE_INFO ==‘파주시티투어’:
        icon = Icon(color='yellow', icon='info-sign')
   else:
   break

#itertuples() tuple을 반복하는 객체 반환
# for row in df_final.itertuples():
#     CITYTOUR_COURSE, CITYTOUR_COURSE_INFO, x, y = row[1:]
# print(row)
#Pandas(index=0, CITYTOUR_COURSE_INFO=‘가평순환코스’, addr=‘가평군’, 위도=37.8245457, 경도=127.5154443)
#Pandas(index=1, CITYTOUR_COURSE_INFO=‘이천시티투어’, addr=‘이천시’, 위도=37.8245457, 경도=127.5154443)

#map 좌표 click시 popup Marker 설정하기
#map 저장하기
# Marker(location=[위도,경도], popup=f'설치위치 : {설치위치}', icon = icon)
#         .add_to(base_map)
#     base_map.save('./data/citytourInfo04.html')
#     return base_map

#map 시각화하기
# citytour_map()
