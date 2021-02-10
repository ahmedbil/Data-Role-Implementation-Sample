import numpy as np
import pandas as pd
from math import*

###########################################
# 1. Clean Up                             #
###########################################

##Initializing the data frame based on data collected from DataSample.csv
data_sample = pd.read_csv('./DataSample.csv')

##Mutating data_sample by dropping duplicates based on suspicous data described
data_sample = (data_sample.drop_duplicates(subset = [' TimeSt', 'Country', 'Province', 'City'],
                                         keep = False))
## Outputing the data frame of data_sample after removing all duplicates
print("The following is the data after cleaning up the data: \n")
print(data_sample)

data_sample = data_sample.reset_index(drop = True)
###########################################
# 2. Label                                #
###########################################

## distance(lon1, lat1, lon2, lat2) calculates the distance between 2 points
def distance(lon1, lat1, lon2, lat2):
    d = sqrt((lon2 - lon1)**2 + (lat2 - lat1)**2)
    return d

##Initializing the data frame based on data collected from POIList.csv
poi_data_list = pd.read_csv('./POIList.csv')


##Creating new columns to assign POI and its distance to the requested address based on minimum distance
data_sample.loc[:,'Associated POI'] = "NaN"
data_sample.loc[:, 'Distance POI'] = "NaN"


## num_rows_ds is the length of the data_sample
num_rows_ds = len(data_sample)

## Assigning POI with minimum distance from each request to its corresponding request address

for i in range(0, num_rows_ds):
    dummy_poi = poi_data_list
    dummy_poi.loc[:, 'Distance'] = 'NaN'
    dummy_poi['Longitude Address'] = data_sample.iloc[i]['Longitude']
    dummy_poi['Latitude Address'] = data_sample.iloc[i]['Latitude']

    for j in range(0, len(dummy_poi)):
        lon1 = dummy_poi.iloc[j]['Longitude']
        lat1 = dummy_poi.iloc[j][' Latitude']
        lon2 = dummy_poi.iloc[j]['Longitude Address']
        lat2 = dummy_poi.iloc[j]['Latitude Address']
        potential_distance = distance(lon1, lat1, lon2, lat2)
        dummy_poi.loc[j, 'Distance'] = potential_distance
        
    data_sample.iloc[i, data_sample.columns.get_loc('Distance POI')] = dummy_poi['Distance'].min()
    indexer = dummy_poi[dummy_poi['Distance'] == dummy_poi['Distance'].min()].index.values
    
    poi_address = dummy_poi.iloc[indexer[0]]['POIID']
    
    data_sample.iloc[i, data_sample.columns.get_loc('Associated POI')] = poi_address


## Exporting the results obtained from above into a new .csv file
data_sample.to_csv(r'C:\Users\ahmed\Desktop\DataRole1\export_dataframe.csv', index = False, header = True)



###########################################
# 3. Label: Part 1)                       #
###########################################


# average_distance(dataframe) calculates the average value in the dataframe's ['Distance POI'] column 
# requires: dataframe contains 'Distance POI' column and contains numeric values
def average_distance(dataframe):
    total_distance = 0
    total_values = 0
    average_distance = 0

    total_distance = dataframe['Distance POI'].sum()
    total_values = len(dataframe)
    return (total_distance / total_values)
        

# standard_deviation(series) calculates the standard deviation of series
# requires: series contains numeric values
def standard_deviation(series):
    std_dev = series.std()
    return std_dev




##Initializing a new data frame based on data collected from exported results in export_dataframe.csv
#Please use the file export_dataframe.csv attached
poi_analysis = pd.read_csv('./export_dataframe.csv')

print("The following is the DataSample with assinged POI's to each request address: \n")
print(poi_analysis)

## POI1:
## setting poi_1 as a split of poi_analysis, conatining all rows with, 'Associated POI' column containing "POI1" point of interest
poi_1 = poi_analysis[poi_analysis["Associated POI"] == "POI1"].copy()
poi_1 = poi_1.reset_index(drop = True)

## setting poi_dis_1 as a split of poi_1, conatining only 'Associated POI', 'Distance POI' columns
poi_dis_1 = poi_1[['Associated POI', 'Distance POI']].copy()


## POI2:

# Since POI2 has the same longitude and latitude as POI1, POI2 will hold the same properties as POI 1
poi_2 = poi_1
poi_dis_2 = poi_1[['Associated POI', 'Distance POI']].copy()

## POI3:

## setting poi_3 as a split of poi_analysis, conatining all rows with, 'Associated POI' column containing "POI3" point of interest
poi_3 = poi_analysis[poi_analysis["Associated POI"] == "POI3"].copy()
poi_3 = poi_3.reset_index(drop = True)

## setting poi_dis_3 as a split of poi_3, conatining only 'Associated POI', 'Distance POI' columns
poi_dis_3 = poi_3[['Associated POI', 'Distance POI']].copy()


## POI4
## setting poi_4 as a split of poi_analysis, conatining all rows with, 'Associated POI' column containing "POI4" point of interest
poi_4 = poi_analysis[poi_analysis["Associated POI"] == "POI4"].copy()
poi_4 = poi_4.reset_index(drop = True)

## setting poi_dis_4 as a split of poi_4, conatining only 'Associated POI', 'Distance POI' columns
poi_dis_4 = poi_4[['Associated POI', 'Distance POI']].copy()

        
#Average Distance of Each POI
avg_dis_poi_1 = average_distance(poi_1)
avg_dis_poi_2 = average_distance(poi_2)
avg_dis_poi_3 = average_distance(poi_3)
avg_dis_poi_4 = average_distance(poi_4)

#Standard Deviation of Each POI
std_dev_poi_1 = standard_deviation(poi_dis_1['Distance POI'])
std_dev_poi_2 = standard_deviation(poi_dis_2['Distance POI'])
std_dev_poi_3 = standard_deviation(poi_dis_3['Distance POI'])
std_dev_poi_4 = standard_deviation(poi_dis_4['Distance POI'])

print("The average distance between POI1 and its assigned requests is: ", avg_dis_poi_1)
print("The average distance between POI1 and its assigned requests is: ", avg_dis_poi_2)
print("The average distance between POI1 and its assigned requests is: ", avg_dis_poi_3)
print("The average distance between POI1 and its assigned requests is: ", avg_dis_poi_4)

print("The standard deviation between POI1 and its assigned requests is: ", std_dev_poi_1)
print("The standard deviation between POI1 and its assigned requests is: ", std_dev_poi_2)
print("The standard deviation between POI1 and its assigned requests is: ", std_dev_poi_3)
print("The standard deviation between POI1 and its assigned requests is: ", std_dev_poi_4)











    
    
    
