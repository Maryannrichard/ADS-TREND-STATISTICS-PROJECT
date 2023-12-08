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
    with one being the original data having years as columns
    and the second being the transposed off the first data having 
    multi-index columns

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
file_path = 'World_Development_Indicators.xlsx'
index_column = ['Country Name','Series Name']

# using the defined function to read the dataframes
df,df_T = read_file(file_path, index_column)

# Checking the first 5 rows of the data df
print('The first 5 rows of the original data df')
print(df.head(5))
print('-----------------------------------')
print('The first 5 rows of the transposed data df_T')
print(df_T.head(5))

# performing data preprocessing on the transposed data df

# removing unwanted columns from the transposed data df_T
df_T = df_T.drop(['Country Code', 'Series Code'], axis=0)

# checking for the data types
df_T.info()

# changing the data types to floats.
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

# reducing the length of series name
series_rename = {
    'Arable land (% of land area)':'Arable land',
    'Forest area (% of land area)':'Forest Area',
    'Renewable energy consumption (% of total final energy consumption)':
        'Renewable Energy Consump',
    'Total greenhouse gas emissions (kt of CO2 equivalent)':
        'Green house gas emissions'
}

df_T = df_T.rename(series_rename, axis=1, level=1)

# creating dataframes for each of the series for use in visualizing.
df_Arable_land = df_T.xs('Arable land', level=1, axis=1)
df_Forest_Area = df_T.xs('Forest Area', level=1, axis=1)
df_CO2 = df_T.xs('CO2 emissions (kt)', level=1, axis=1)
df_Renewable_Energy = df_T.xs('Renewable Energy Consump', level=1, axis=1)
df_Pop = df_T.xs('Population growth (annual %)', level=1, axis=1)
df_Green_house = df_T.xs('Green house gas emissions', level=1, axis=1)

# plotting a line gragh for the new dataframes

plt.figure()

# Ist subplot: Arable Land
plt.subplot(2,2,1)
df_Forest_Area.iloc[::].plot(kind='line', style='--')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Arable land (% of land area) ')
plt.xlabel('Year')
plt.savefig('Arable land.png')
plt.show();





