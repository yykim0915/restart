import pandas as pd
import os
import webbrowser
import folium
#from folium.plugins import MakerCluster


latitude = 37.564345 #위도
longitude = 126.974385 #경도

map_osm = folium.Map(location=[latitude, longitude], zoom_start=12)
# folium.Marker([latitude, longitude], icon=folium.Icon('red', icon='star'), popup='덕수궁', tooltip='big data').add_to(map_osm)
folium.Marker([latitude, longitude],
              icon=folium.Icon(color='red', icon='star'), #popup='덕수궁',
              popup='<iframe width="500" height="300" src="https://www.daum.net/" title="daum사이트" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
              tooltip='big data').add_to(map_osm)

folium.CircleMarker([latitude, longitude],
                    #color='tomato', fill_color='pink',
                    color='#3186ff',   fill_color='#3186ff', radius = 100,
                    tooltip='big data').add_to(map_osm)

map_osm.save('./data/map01.html')
webbrowser.open('file://'+ os.path.realpath('./data/map01.html'))
print('map01 save')
