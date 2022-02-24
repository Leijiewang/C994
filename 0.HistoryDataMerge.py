# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:33:29 2021

@author: ljwang
"""
#表一表二
import pandas as pd
old = pd.read_excel(r".\inputdata\107-109高風險路廊事故資料_20210805.xlsx", sheet_name="表一")
columnname = list(old.columns)
new = pd.read_excel(r".\inputdata\110年全年資料庫去個資-資料更新至1101031.xlsx", sheet_name="表一", usecols=columnname)
en_columnname=['CaseID', 'Date', 'Time', 'Year', 'Month', 'Week'
               , 'PositionLon', 'PositionLat', 'Case_category', 'Accident_category '
               , 'Jurisdiction_code', 'Addresstype_code', 'Addresstype','CityCode', 'CityName', 'TownCode'
               , 'TownName','Village_code', 'Village', 'Neighborhood', 'Street_code', 'Street', 
               'Section', 'Lane', 'Alley', 'Number', 'Meters', 'Side', 'Village_junc', 'Street_junc', 
               'Section_junc', 'Lane_junc', 'Alley_junc', 'Others', 'Road_code', 'Road_category', 
               'Road_number', 'Road', 'Road_km', 'Road_meters', 'Road_direction', 'Road_lane_code', 
               'Road_lane', 'Railway_route_code', 'Railway_route', 'Railway_line_code', 'Railway_line', 
               'Railway_km', 'Railway_meters', 'Railway', 'Railway_others', 'Deaths_24hr', 
               'Deaths_2-30days', 'Injured', 'Weather_code', 'Weather', 'Light_code', 'Light', 
               'Firstparty_road_code', 'Firstparty_road', 'Firstparty_speed\u200b\u200blimit', 
               'Roadtype_code', 'Roadtype', 'Roadtype_code_sub', 'Roadtype_sub', 'Aclocation_code', 
               'Aclocation', 'Aclocation_code_sub', 'Aclocation_sub', 'Pavement_code', 'Pavement', 
               'Roadcondition_code', 'Roadcondition', 'Pavementdefect_code', 'Pavementdefect', 
               'Obstacle_code', 'Obstacle', 'Sightquality_code', 'Sightquality', 'Sight_code', 
               'Sight', 'signals_code', 'signals', 'signalaction_code', 'signalaction', 
               'Branchfacility_code', 'Branchfacility', 'Branchfacility_code_sub', 
               'Branchfacility_sub', 'Lanefacility_code', 'Lanefacility', 'Lanefacility_speed_code', 
               'Lanefacility_speed', 'Pavementedge_code', 'Pavementedge', 'Actype_code', 'Actype', 
               'Actype_code_sub', 'Actype_sub', 'Cause_code', 'Cause', 'Cause_code_sub', 'Cause_sub', 
               'Cause_a3', 'Phase_code_a3', 'Phase_a3', 'Rest_a3']
old.columns = en_columnname
new.columns = en_columnname
res=pd.concat([old, new])
res = res.loc[res["TownName"]== "屏東市"]
res.index=range(len(res))
res.to_excel(r".\outputdata\107to11010表一.xlsx", index=False)
#表二資料合併
old = pd.read_excel(r".\inputdata\107-109高風險路廊事故資料_20210805.xlsx", sheet_name="表二")
columnname = list(old.columns)
new = pd.read_excel(r".\inputdata\110年全年資料庫去個資-資料更新至1101031.xlsx", sheet_name="表二", usecols=columnname)
en_columnname=['CaseID', 'Parties_order', 'Nationality', 'Gender_code', 'Gender', 'Age', 'Cartype_code', 'Cartype', 'Cartype_code_sub', 'Cartype_sub', 'license_code', 'license', 'Cause', 'Injury_code', 'Injury', 'Maininjury_code', 'Maininjury', 'Equipment_code', 'Equipment', 'Ecequipment_code', 'Ecequipment', 'Use_code', 'Use', 'Action_code', 'Action', 'Action_code_sub', 'Action_sub', 'Qualification_code', 'Qualification', 'Licensetype_code', 'Licensetype', 'Licensetype_code_sub', 'Licensetype_sub', 'Drinking_code', 'Drinking', 'Impactsite_code', 'Impactsite', 'Impactsite_code_sub', 'Impactsite_sub', 'Impactsite_code_other', 'Impactsite_other', 'Impactsite_code_sub_other', 'Impactsite_sub_other', 'Causejudge_code', 'Causejudge', 'Causejudge_code_sub', 'Causejudge_sub', 'Hitandrun_code', 'Hitandrun', 'Profession_code', 'Profession', 'Trippurpose_code', 'Trippurpose']
old.columns = en_columnname
new.columns = en_columnname
res=pd.concat([old, new])
res.index=range(len(res))
res.to_excel(r".\outputdata\107to11010表二.xlsx", index=False)
