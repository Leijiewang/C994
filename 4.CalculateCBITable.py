# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:16:05 2021

@author: ljwang
"""
#3hr
import pandas as pd

path = r".\outputdata\RoadSafty_11.xlsx"
first = pd.read_excel(path, sheet_name="表一")
environment = pd.read_excel(path, sheet_name="事故環境")
safty = pd.read_excel(r".\outputdata\Safty_11月.xlsx")
sta = pd.read_excel(r".\outputdata\STA_11月.xlsx")#原始

# #案件數處理

def calculat_cases(topic, year, datasafty, junid, month):
    # print(f"cases:{junid}")
    #全部都必須篩junid
    data = datasafty.loc[datasafty["id"] == junid]
    #案條件篩
    if year!= "ALL":
        data = data.loc[data["year"] == year]
    if month!= "ALL":
        data = data.loc[data["Month"] == month]  
    if topic!= "ALL":
        data = data.loc[data[topic] == 1]
    data.index = range(len(data))
    accident = len(data)
    return pd.Series([accident])

def filterdata(topic, year, datasafty, junid, month):
    #全部都必須篩junid
    data = datasafty.loc[datasafty["id"] == junid]
    #案條件篩
    if year!= "ALL":
        data = data.loc[data["year"] == year]
    if month!= "ALL":
        data = data.loc[data["Month"] == month]  
    if topic!= "ALL":
        data = data.loc[data[topic] == 1]
    data.index = range(len(data))
    accident = len(data)
    return data

def people(topic, year, datasafty, junid, firstdata, month):
    data = filterdata(topic, year, datasafty, junid, month)
    death = 0
    injury = 0  

    data2 = pd.merge(data, first, on="CaseID", how="left")
    data3 = data2.groupby(["TownName"]).sum()
    data3.index = range(len(data3))
    
    if len(data2) > 0:
        death = data3["Deaths_24hr"][0]+data3["Deaths_2-30days"][0]
        injury = data3["Injured"][0]
    else:
        death = 0
        injury = 0
    return pd.Series([death, injury])

def AcClass(topic, year, datasafty, junid, firstdata, month):
    data = filterdata(topic, year, datasafty, junid, month)
    acclass=[]
    for i in range(0, len(data)):
        data2 = environment.loc[environment["CaseID"] == data["CaseID"][i]]
        data2.index=range(len(data2))
        acclass.append(data2["Series"][0])
    numa1 = acclass.count("A1")
    numa2 = acclass.count("A2")
    numa3 = acclass.count("A3")        
    return pd.Series([numa1, numa2, numa3])

def timesandcause(topic, year, datasafty, junid, firstdata, month):
    data = filterdata(topic, year, datasafty, junid, month)
    causename = []
    causetimes = []
    for i in range(0, len(data)):
        data2 = firstdata.loc[firstdata["CaseID"] == data["CaseID"][i]]
        data2.index=range(len(data2))
        causename.append(data2["Cause_sub"][0])
    setcause = set(causename)
    setcause = list(setcause)
    if " " in setcause:
        setcause.remove(" ")            
    for p in range(0, len(setcause)):
        causetimes.append(causename.count(setcause[p]))
    ctt = {}
    ctt["cause"] = setcause
    ctt["frequency"] = causetimes    
    return pd.Series([ctt])

def rain(topic, year, datasafty, junid, firstdata, month):
    data = filterdata(topic, year, datasafty, junid, month)
    rainhour = 0
    rainday = 0
    for i in range(0, len(data)):
        rainhour += data["hourly_of_precipitation"][i]
        rainday += data["daily_of_precipitation"][i]
    return pd.Series([rainhour,rainday])

def main1(topic, year, datasafty, junid, firstdata, month):
    print(f"main1:{topic},{year},{junid}")
    accident = calculat_cases(topic, year, datasafty, junid, month)
    DeadandInjury = people(topic, year, datasafty, junid, firstdata, month)
    A1A2A3 = AcClass(topic, year, datasafty, junid, firstdata, month)
    causedic = timesandcause(topic, year, datasafty, junid, firstdata, month)
    resrain = rain(topic, year, datasafty, junid, firstdata, month)
    recolumns = pd.concat([accident, DeadandInjury, A1A2A3, causedic, resrain], axis=0, ignore_index=True)
    return recolumns

sta[["cases", "deaths", "injuries", "A1", "A2", "A3", "CauseFrequency", "RainfallHour", "RainfallDaily"]] = sta.apply(lambda x : main1(x["Project"], x["Year"], safty, x["JunctionID"], first, x["Month"]), axis=1)

#CBI計算#epdo
def calepdo(a, b, c):   
    return a*9.5+b*3.5+c
sta["epdo"] = sta.apply(lambda x : calepdo(x["deaths"], x["injuries"], x["cases"]), axis=1)
# sta.to_excel(".\outputdata\sta_tmp.xlsx")

data2 = sta.groupby(["Year", "Month", "Project"])

data4 = pd.DataFrame()
combination = list(data2.indices.keys())
def CBI(a,b):
    return a+b
for c in combination:
    data3 = data2.get_group(c)
    data3.index = range(len(data3))
    
    maxcases = data3["cases"].max()
    maxepdo = data3["epdo"].max()     

    data3["SRI"] = data3["cases"].apply(lambda x: float(x)/float(maxcases) if  maxcases!=0 else "")
    data3["SSI"] = data3["epdo"].apply(lambda x: x/maxepdo if maxepdo!=0 else "")        
    data3["CBI"] = data3.apply(lambda x: CBI(x["SRI"], x["SSI"]), axis=1)
    
    data4 = pd.concat([data4, data3])
 
sta = data4.copy()
sta.to_excel(r".\outputdata\res_STA_11月.xlsx", index=False)
#把cases=0刪掉，減少資料
# sta=data3.copy()
# sta=sta.loc[sta["cases"]>0]
# sta.index=range(len(sta))
#A1、A2、A3人數

# sta.to_excel(".\outputdata\sta_tmp3.xlsx")
#每月次數
# def CaseMonth(topic,year,datasafty,junid,month):
#     data=filterdata(topic,year,datasafty,junid,month)
#     record_month=[]
#     casenum=[]
#     for i in range(0,len(data)):
#         string=data["CaseID"][i][3:5]
#         nummonth=int(string)
#         record_month.append(nummonth)
#         print(record_month)
#     for p in range(1,13):
#         numcase=record_month.count(p)
#         casenum.append(numcase)

#     return casenum
# rescbm=[]
# for i in range(0,len(sta)):#len(sta)
#     print(f"CaseByMonth:{i}")
#     casebymonth=CaseMonth(sta["Project"][i],sta["Year"][i],safty,sta["Junction_ID"][i],sta["month"][i])       
#     cbm={}
#     cbm["month"]=[x for x in range(1,13)]
#     cbm["cases"]=casebymonth
#     rescbm.append(cbm)
#     # sta["CaseByMonth"][i]=cbm
# sta["CaseByMonth"]=rescbm
# sta.to_excel(".\outputdata\1202_sta.xlsx")