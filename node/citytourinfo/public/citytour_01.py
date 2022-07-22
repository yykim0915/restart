# from bottle import route, run
from bottle import route, run, error, static_file, template, request, response, view
import pymysql
import pandas as pd
import folium
import base64
import json
import requests

#mongodbCompass
from pymongo import MongoClient
client = MongoClient("mongodb://3.38.64.25:27017")
db = client['st_db']

# for d in db['accom_tb'].find():
#     print(d['sg_cd'], d['ac_name'])


@route('/')
@route('/map')
@route('/map/<i_sg_cd>')
def index(i_sg_cd='41820+'):


     




run(host='0.0.0.0', port=8080, threaded=True)
