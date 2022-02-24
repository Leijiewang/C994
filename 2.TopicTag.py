# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:46:27 2021

@author: ljwang
"""

import pandas as pd

#read file
path = r".\outputdata\RoadSafty_11.xlsx"
tmp = pd.read_excel(path, sheet_name = "事故環境", usecols=["CaseID", "id", "Month", "hourly_of_precipitation", "daily_of_precipitation", "Hour"])
tmp = tmp.loc[tmp["id"].notnull()]
tmp = tmp.drop_duplicates().reset_index()
safty = tmp[["CaseID", "id", "Month", "hourly_of_precipitation", "daily_of_precipitation", "Hour"]]

secondcol = ["CaseID","Injury_code","Cartype_code","Age","Cartype_code_sub"]
second=pd.read_excel(path,sheet_name = "表二", usecols = secondcol)
second['Injury_code'] = second['Injury_code'].astype(str)
second['Cartype_code'] = second['Cartype_code'].astype(str)
# second['Age'] = second['Age'].astype(int)

first=pd.read_excel(path, sheet_name = "表一")


#新增專案
def topic_ped(id, data):
    
    print(f"ped:{id}")
    data = data.loc[data["CaseID"]== id]
    data = data.loc[data["Cartype_code_sub"]== "H01"]
    data.index=range(len(data))
    if len(data) > 0:
        a = 1
    else:
        a = 0
    return a
def topic_elder(id, data):
    print(f"elder:{id}")
    data = data.loc[data["CaseID"]== id]
    data = data.loc[data["Injury_code"]!="3"]
    data = data.loc[data["Injury_code"]!="4"]
    data = data.loc[data["Injury_code"]!=" "]
    data = data.loc[65<=data["Age"]]
    data.index=range(len(data))
    if len(data) > 0:
        a = 1
    else:
        a = 0
    return a

def topic_young(id, data):
    print(f"young:{id}")
    data = data.loc[data["CaseID"]== id]
    data = data.loc[data["Cartype_code"]=="C0"]
    data = data.loc[18<=data["Age"]]
    data = data.loc[data["Age"]<=24]
    data.index=range(len(data))
    if len(data) > 0:
        a = 1
    else:
        a = 0
    return a    

def main(id, data):
    a = topic_ped(id, data)
    b = topic_elder(id, data)
    c = topic_young(id, data)
    return pd.Series([a, b, c])

safty[["ped", "elder", "young"]] = safty["CaseID"].apply(lambda x : main(x, second))


def year(id):
    print(f"year:{id}")
    if id[0:3]=="107":
        stryear=2018
    elif id[0:3]=="108":
        stryear=2019
    elif id[0:3]=="109":
       stryear=2020
    elif id[0:3]=="110":
        stryear=2021
    return stryear
safty["year"] = safty["CaseID"].apply(lambda x : year(x))
safty.to_excel(r".\outputdata\Safty_11月.xlsx", index=False)
# print(list(second.columns))
# second=second.loc[:,secondcol]
# rain=pd.read_excel(r".\inputdata\道路安全資料_11月.xlsx",sheet_name="事故環境")
# activity=pd.read_csv(r".\outputdata\junction_F.csv")

# holiday=pd.read_csv(r"D:\desktop\holiday.csv")
# temp=[]
# for i in range(0,len(holiday)):
#     print(i)
#     string=holiday["date"][i].split("/")
#     year2=int(string[0])
#     month=int(string[1])
#     day=int(string[2])
#     if month<10:
#         month="0"+str(month)
#     if day<10:
#         day="0"+str(day)
#     result=str(year2)+str(month)+str(day)
#     temp.append(result)
# holiday["date"]=temp


#觀光

# for i in range(0,len(safty)):#len(safty)
#     print(i)
#     if activity["Number_of_Spots"][safty["Junction_ID"][i]] ==0:
#         play.append(0)
#     elif activity["Number_of_Spots"][safty["Junction_ID"][i]]>0:        
#         temp = safty.loc[safty["Junction_ID"] == safty["Junction_ID"][i]]        
#         temp.index=range(len(temp))
#         kk=[]
#         for p in range(0,len(temp)):
#             temp2 = first.loc[first["CaseID"]==temp["CaseID"][p]]
#             temp2.index=range(len(temp2))
#             compare=list(holiday["date"])
#             if str(temp2["Date"][0]) in compare:
#                 kk.append(1)
#             else:
#                 kk.append(0)
#         if max(kk)==1:
#             play.append(1)
#         else:
#             play.append(0)

# safty["sightseeing"]=play
# hour=[]
# day=[]
# #rainfall
# for i in range(0,len(safty)):
#     temp=rain.loc[rain["CaseID"]==safty["CaseID"][i]]
#     temp=temp.loc[temp["JunctionID"]==safty["Junction_ID"][i]]
#     temp.index=range(len(temp))
#     hour.append(temp["RainfallHour"][0])
#     day.append(temp["RainfallDaily"][0])
# safty["RainfallHour"]=hour
# safty["RainfallDaily"]=day
# #事件是不是假日
# holiday=[]
# for i in range(0,len(safty)):
#     id=safty["CaseID"][i]
#     temp2 = first.loc[first["CaseID"]==id]
#     temp2.index=range(len(temp2))
#     if str(temp2["Date"][0]) in compare:
#         holiday.append(1)
#     else:
#         holiday.append(0)
    
# safty["Holiday"]=holiday

# #事件時間
# hourtime=[]
# for i in range(0,len(safty)):
#     print(i)
#     temp=rain.loc[rain["CaseID"]==safty["CaseID"][i]]
#     temp=temp.loc[temp["JunctionID"]==safty["Junction_ID"][i]]
#     temp.index=range(len(temp))
#     hourtime.append(temp["Hour"][0])
# safty["Hour"]=hourtime


# safty.to_excel(r".\outputdata\1202_safty.xlsx")
