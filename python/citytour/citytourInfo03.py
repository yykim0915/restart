import pandas as pd
import openpyxl
from statistics import mean


# fname='./data/citytour.xlsx'
# sam = pd.ExcelFile(fname)
# print(sam)

filePath = r'./data/citytour.xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')
df_from_excel.columns = df_from_excel.loc[0].tolist()
print(df_from_excel.head())
print(df_from_excel['SIGNGU_NM'].values)
print(df_from_excel['CITYTOUR_COURSE_NM'].values)
print(df_from_excel['CITYTOUR_COURSE_INFO'].values)
print(df_from_excel['위도'].values)
print(df_from_excel['경도'].values)
