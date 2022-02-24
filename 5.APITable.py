# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:28:16 2021

@author: ljwang
"""

#變成能套用至儀表板的欄位名稱
import pandas as pd

path = r".\outputdata\RoadSafty_11.xlsx"

columnname = ['JunctionID', 'Name', 'PositionLon', 'PositionLat', 'Stops', 'Routes', 'Stopsinfo',
              'Spots', 'SpotInfos', 'SpotsAvgDist', 'Restaurants', 'RestAvgDist',
              'Hotels', 'HotelsAvgDist', 'Parkings', 'ParkingsAvgDist', 'Exits',
              'TotalSpaces', 'Schools', 'SchoolAvgDist', 'NearestSchool', 'Hospitals',
              'HospitalsAvgDist', 'NearestHospitals', 'Branches', 'Angle',
              'GasStation', 'Markets', 'MarketsAvgDist', 'NearestMarket']
junction = pd.read_excel(path, sheet_name = "路口特性", usecols = columnname)
sta = pd.read_excel(r".\outputdata\res_STA_11月.xlsx")

res = pd.merge(sta, junction, on="JunctionID", how="left")

newcolumnname = ['JunctionID', 'Year', 'Month', 'Project', 'cases', 'deaths', 'injuries', 'CBI', 
                 'A1', 'A2', 'A3', 'CauseFrequency', 'RainfallHour', 'RainfallDaily',
                 'Name', 'PositionLon', 'PositionLat', 'Branches', 'Stops', 'Stopsinfo', 'Angle', 
                 'Routes', 'Parkings', 'Exits', 'TotalSpaces', 'Spots', 'Hotels', 'Schools', 'Restaurants',
                 'Hospitals', 'GasStation', 'Markets']
res = res[newcolumnname]

res.rename(columns={'JunctionID': 'Junction_ID', 'Month': 'month'}, inplace=True)


res.to_excel(r".\outputdata\APIOUTPUT_11月v5.xlsx")