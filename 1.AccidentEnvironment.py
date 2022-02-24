# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:52:19 2021

@author: ljwang
"""

import pandas as pd

one = pd.read_excel(r".\outputdata\107to11010表一.xlsx")
two = pd.read_excel(r".\outputdata\107to11010表二.xlsx")
junction = pd.read_excel(r".\inputdata\路口特性.xlsx")
o_columnname =['CaseID', 'hourly_of_precipitation', 'Visibility', 'daily_of_precipitation',  
              'junction_coordinate', 'id','Series', 'Hour', 'Date','Month']
tmp = pd.read_excel(r".\inputdata\事故趨勢儀表板資料3.xlsx", usecols=o_columnname)

def geopoint(string):
    string = str(string).split(",")
    if len(string) ==2:
        lon=string[0][1:-1]
        lat=string[1][1:-2]
    else:
        lon=""
        lat=""
    return lon, lat

tmp["PositionLon"] = tmp["junction_coordinate"].apply(lambda x : geopoint(x)[0])
tmp["PositionLat"] = tmp["junction_coordinate"].apply(lambda x : geopoint(x)[1])
del tmp["junction_coordinate"]

with pd.ExcelWriter('.\outputdata\RoadSafty_11.xlsx') as writer:
    one.to_excel(writer, sheet_name='表一')
    two.to_excel(writer, sheet_name='表二')
    tmp.to_excel(writer, sheet_name='事故環境')
    junction.to_excel(writer, sheet_name='路口特性')