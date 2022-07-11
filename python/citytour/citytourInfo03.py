import pandas as pd
import folium
#import openpyxl


filePath = r'./data/citytour.xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')
#df_from_excel = pd.read_excel(filePath,engine='openpyxl',header=None)

df_from_excel.columns = ['CITYTOUR_COURSE_INFO','addrs','x','y']

name_list = df_from_excel['CITYTOUR_COURSE_INFO'].to_list()
addr_list = df_from_excel['addrs'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

map = folium.Map(location=[37,127],zoom_start=7)

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i],position_x_list[i]],
                            popup=name_list[i],
                            icon = folium.Icon(color='blue'))
        marker.add_to(map)

map.save(r'./data/map_citytourInfo03.html')
