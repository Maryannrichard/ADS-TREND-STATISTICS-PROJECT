# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:21:33 2023

@author: MARYANN
"""

# importing necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import stats as sta

# Writing a function for use in reading the data

def read_file(file_path, index_column):
    '''
    This function reads a dataframe and returns 2 dataframes
    with one being the original data and the second being the 
    transposed off the first data having  multi-index columns

    Parameters:
    ------------------
    file_path : The name of the file to be read
    index_column : setting some columns as index

    Returns:
    ------------------
    df : The original data
    df_T: The transposed data

    '''
    # Read the file into a DataFrame
    df = pd.read_excel(file_path)

    # Set a specified column as the index
    df.set_index(index_column, inplace=True)

    # Transpose the DataFrame
    df_T = df.T
    
    # call the dataframes to be returned
    return df, df_T

# defining the augments for the function to take
file_path = 'World_Development_Indicators (1).xlsx'
index_column = ['Country Name','Series Name']

# using the defined function to read the dataframes
df,df_T = read_file(file_path, index_column)

# Check the first 5 rows of the returned dataframes
print('The first 5 rows of the original data df')
print(df.head(5))
print('-----------------------------------')
print('The first 5 rows of the transposed data df_T')
print(df_T.head(5))

# performing data preprocessing on the transposed data df

# removing unwanted columns from the transposed data df_T
df_T = df_T.drop(['Country Code', 'Series Code'], axis=0)

# check for the data types
df_T.info()

# change the data types to floats.
df_T = df_T.astype(float)

# checking for null values in the transposed data df_T
df_T.isna().sum()

# Removing the NaN data in the transposed data df_T
df_T.dropna(axis=1, how='all', inplace=True)

# renaming df_T dataframe Year row
year_rename = {
    '2008 [YR2008]': 2008,
    '2009 [YR2009]': 2009,
    '2010 [YR2010]': 2010,
    '2011 [YR2011]': 2011,
    '2012 [YR2012]': 2012,
    '2013 [YR2013]': 2013,
    '2014 [YR2014]': 2014,
    '2015 [YR2015]': 2015,
    '2016 [YR2016]': 2016,
    '2017 [YR2017]': 2017,
    '2018 [YR2018]': 2018,
    '2019 [YR2019]': 2019,
    '2020 [YR2020]': 2020
}

df_T = df_T.rename(year_rename,axis=0)

# reducing the length of some series name
series_rename = {
    'Arable land (% of land area)':'Arable land',
    'Forest area (% of land area)':'Forest Area',
    'Renewable energy consumption (% of total final energy consumption)':
        'Renewable Energy Consump',
    'Total greenhouse gas emissions (kt of CO2 equivalent)':
        'Green house gas emissions'
}

df_T = df_T.rename(series_rename, axis=1, level=1)

# reducing the length of some country names
new_name = {'Russian Federation':'Russia'}
df_T = df_T.rename(new_name, axis=1, level=0)

# creating dataframes for each of the series for use in visualizing.
df_Arable_land = df_T.xs('Arable land', level=1, axis=1)
df_Forest_Area = df_T.xs('Forest Area', level=1, axis=1)
df_CO2 = df_T.xs('CO2 emissions (kt)', level=1, axis=1)
df_Renewable_Energy = df_T.xs('Renewable Energy Consump', level=1, axis=1)
df_Urban_Pop = df_T.xs('Urban population (% of total population)', 
                       level=1, axis=1)
df_Green_house = df_T.xs('Green house gas emissions', level=1, axis=1)

# plotting a line gragh for the new dataframes for all countries

# Ist plot: Forest Area
plt.figure()
df_Forest_Area.iloc[::].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Forest area (% of land area) ')
plt.savefig('lineplot Forest Area.png')
plt.show();

# 2nd plot: Arable land
plt.figure()
df_Arable_land.iloc[::].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Arable land (% of land area) ')
plt.savefig('lineplot Arable land.png')
plt.show();

# 3rd plot: CO2 Emissions
plt.figure()
df_CO2.iloc[::].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('CO2 emissions (kt)')
plt.savefig('lineplot CO2 emissions (kt).png')
plt.show();

# 4th plot: Total greenhouse gas emissions
plt.figure()
df_Green_house.iloc[::].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Total greenhouse gas emissions (kt of CO2 equivalent)')
plt.savefig('lineplot CO2 emission.png')
plt.show();

#5th plot: Urban Population growth
plt.figure()
df_Urban_Pop.iloc[::].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Urban population (% of total population)')
plt.savefig('lineplot Urban population growth.png')
plt.show();

#6th plot: Renewable Energy Consumption
plt.figure()
df_Renewable_Energy.iloc[::].plot(kind='line', style='--')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.xlabel('Year')
plt.title('Renewable energy consumption(% of total final energy consumption)')
plt.savefig('lineplot renewable energy.png')
plt.show();

# plot of barcharts for comparism among the series over the years by country

# 1st plot: Urban Population growth
plt.figure(figsize=(20,15))
df_Urban_Pop.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.title('Urban population (% of total population)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot Urban Population growth.png')
plt.show()

# 2nd plot: CO2 emission
plt.figure(figsize=(20,15))
df_CO2.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.title('CO2 emissions (kt)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot CO2 emission.png')
plt.show()

# 3rd plot: Arable land
plt.figure(figsize=(20,15))
df_Arable_land.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=45)
plt.title('Arable land (% of land area)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot Arable land.png')
plt.show()

# 4th plot: Renewable Energy
plt.figure()
df_Renewable_Energy.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Renewable energy consumption(% of total final energy consumption)')
plt.savefig('Barplot REnewable Energy.png')
plt.show();

# 5th plot: Green house emission
plt.figure()
df_Green_house.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Total greenhouse gas emissions (kt of CO2 equivalent)')
plt.savefig('Barplot Green house emission.png')
plt.show();

#6th plot: Forest Area
plt.figure()
df_Forest_Area.T.iloc[:,0::2].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Forest area (% of land area)')
plt.savefig('Barplot Forest Area.png')
plt.show();











