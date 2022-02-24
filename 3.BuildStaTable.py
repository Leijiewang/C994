# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:28:56 2021

@author: ljwang
"""

import pandas as pd

environment = pd.read_excel(r".\outputdata\Safty_11月.xlsx")
junenvironment = environment[(environment["ped"]!=0) | (environment["elder"]!=0) | (environment["young"]!=0)].reset_index()
junenvironment["id"] = junenvironment["id"].apply(lambda x : int(x))
junenvironment = junenvironment.iloc[:,1:-1]
junlist = list(junenvironment["id"].unique())
yearlist=[2018, 2019, 2020, 2021]
monthlist=[1,2,3,4,5,6,7,8,9,10,11,12,"ALL"]
topiclist=["ped", "elder", "young", "ALL"]

jj=[]
yy=[]
mm=[]
tt=[]
for j in junlist:
    for y in yearlist:
        for m in monthlist:
            for t in topiclist:
                jj.append(j)
                yy.append(y)
                mm.append(m)
                tt.append(t)
                
com=pd.DataFrame(zip(jj, yy, mm, tt),columns=["JunctionID","Year", "Month", "Project"])

com.to_excel(r".\outputdata\STA_11月.xlsx", index=False)