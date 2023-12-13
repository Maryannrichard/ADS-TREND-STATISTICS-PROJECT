# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:21:33 2023

@author: MARYANN
"""

# importing necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import skew, kurtosis

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
file_path = 'World_Development_Indicators (11).xlsx'
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
df_T.dtypes

# change the data types to floats.
df_T = df_T.apply(pd.to_numeric, errors='coerce')

# checking for null values in the transposed data df_T
df_T.isna().sum()

# Removing the NaN data in the transposed data df_T
df_T.dropna(axis=1, how='all', inplace=True)

# renaming df_T dataframe Year row
year_rename = {
    '1995 [YR1995]': 1995,
    '2000 [YR2000]': 2000,
    '2005 [YR2005]': 2005,
    '2010 [YR2010]': 2010,
    '2015 [YR2015]': 2015,
    '2020 [YR2020]': 2020
   }

df_T = df_T.rename(year_rename,axis=0)

print(df_T)

# reducing the length of some series name
series_rename = {
    'Arable land (% of land area)':'Arable land',
    'Forest area (% of land area)':'Forest Area',
    'Renewable energy consumption (% of total final energy consumption)':
        'Renewable Energy',
    'Urban population (% of total population)':'Urban population',
    'GDP growth (annual %)':'GDP'
}

df_T = df_T.rename(series_rename, axis=1, level=1)

# Creating dataframes for 5 of the countries for use in statistical analysis.
Italy = df_T.xs('Italy', level=0, axis=1)
Indonesia = df_T.xs('Indonesia', level=0, axis=1)
United_states = df_T.xs('United States',axis=1,level=0)
India = df_T.xs('India',axis=1, level=0)
China = df_T.xs('China', axis=1, level=0)  

# using the .describe() method for statistical properties

print(f"Statistical description for India:\n")
print(China.describe())

print(f"Statistical decription for United_states:\n")
print(United_states.describe())

print(f"Statistical description for China:\n")
print(China.describe())

# Checking for the skewness of the series of some countries

print(f"Skewness description for China Series:\n")
print(China.skew())

print(f"Skewness description for India Series:\n")
print(India.skew())

print(f"Skewness description for United_states Series:\n")
print(United_states.skew())

# Using Kurtosis to check statistical properties
print(f"Kurtosis Statistical description using kurtosis for United_states:\n")
print(United_states.kurtosis())

print(f"Statistical description using kurtosis for China:\n")
print(China.kurtosis())

print(f"Statistical description using kurtosis for India:\n")
print(India.kurtosis())

# create a heatmap to understand correlation among the series of each country

# 1st plot: China
plt.figure(figsize=(10,8))
 
sns.heatmap(China.corr(),  cbar=True, annot= True,
            cmap='Blues', linewidths =.5,square=True, fmt='.2g',
            annot_kws={'size':14}).set_title('China Series')
plt.savefig('China Series heatmap.png', bbox_inches='tight')
plt.show();

# 2nd plot: India
plt.figure(figsize=(10,8))

sns.heatmap(India.corr(), cbar=True,annot=True,
            square=True,linewidths=.5,
            cmap='Reds',fmt='.2g',
            annot_kws={'size':14}).set_title('India Series')
plt.savefig('India series heapmap.png', bbox_inches='tight')
plt.show();

# 3rd plot: United States
plt.figure(figsize=(10,8))

sns.heatmap(United_states.corr(),cmap='Greens',
            annot_kws={'size':14},cbar=True,
            square=True,fmt='.2g',annot=True,
            linewidths=.5).set_title('United States Series')
plt.savefig('United States series heatmap.png', bbox_inches='tight')
plt.show();

# 4th plot: Italy
plt.figure(figsize=(10,8))

sns.heatmap(Italy.corr(), cbar=True, annot=True,cmap='magma_r',square=True,
            fmt='.2g',annot_kws={'size':14},
            linewidths=.5).set_title('Italy Series')
plt.savefig('Italy Series heatmap.png', bbox_inches='tight')
plt.show();

# 5th plot: Indonesia
plt.figure(figsize=(10,8))

sns.heatmap(Indonesia.corr(), cbar=True, annot=True,cmap='rainbow_r',
            square=True,fmt='.2g', annot_kws={'size':14},
            linewidths=.5).set_title('Indonesia Series')
plt.savefig('Indonesia Series heatmap.png', bbox_inches='tight')
plt.show();


# create dataframes for each of the series for use in visualizing.
df_Arable_land = df_T.xs('Arable land', level=1, axis=1)
df_Forest_Area = df_T.xs('Forest Area', level=1, axis=1)
df_CO2 = df_T.xs('CO2 emissions (kt)', level=1, axis=1)
df_Renewable_energy= df_T.xs('Renewable Energy',level=1, axis=1)
df_Urban_Pop = df_T.xs('Urban population', 
                       level=1, axis=1)
df_GDP= df_T.xs('GDP',level=1, axis=1)


# plotting a line gragh for the new dataframes for all countries

# Ist plot: Forest Area
plt.figure()
df_Forest_Area.iloc[:].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Forest area (% of land area) ')
plt.savefig('line_plot Forest Area.png', bbox_inches='tight')
plt.show();

# 2nd plot: Arable land
plt.figure()
df_Arable_land.iloc[:].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Arable land (% of land area) ')
plt.savefig('lineplot Arable land.png',bbox_inches='tight')
plt.show();

# 3rd plot: CO2 Emissions
plt.figure()
df_CO2.iloc[:].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('CO2 emissions (kt)')
plt.savefig('lineplot CO2 emissions (kt).png', bbox_inches='tight')
plt.show();

# 4th plot: GDP growth(annual %)
plt.figure()
df_GDP.iloc[:].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('GDP growth (annual %)')
plt.savefig('lineplot GDP.png', bbox_inches='tight')
plt.show();

#5th plot: Urban Population growth
plt.figure()
df_Urban_Pop.iloc[:].plot(kind='line', style='--')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Urban population (% of total population)')
plt.savefig('lineplot Urban population growth.png', bbox_inches='tight')
plt.show();

#6th plot: Renewable Energy Consumption
plt.figure()
df_Renewable_energy.iloc[:].plot(kind='line', style='--')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.xlabel('Year')
plt.title('Renewable energy consumption(% of total final energy consumption)')
plt.savefig('lineplot renewable energy.png', bbox_inches='tight')
plt.show();

# plot of barcharts for comparism among the series over the years by country

# creating a color map for the visuals
color= ['blue','red','green','orange','black']
color2=['magenta','cyan','red','gray','yellow']


# 1st plot: Urban Population growth
plt.figure(figsize=(20,15))
df_Urban_Pop.T.iloc[:,:].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.title('Urban population (% of total population)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot Urban Population growth.png',bbox_inches='tight')
plt.show()

# drawing a table to see the Urban population progression over the years
df_urban= df_Urban_Pop.T.iloc[:,:]
print(df_urban)

# 2nd plot: CO2 emission
plt.figure(figsize=(20,15))
df_CO2.T.iloc[:,:].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.title('CO2 emissions (kt)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot CO2 emission.png', bbox_inches='tight')
plt.show()

# 3rd plot: Arable land
plt.figure(figsize=(20,15))
df_Arable_land.T.iloc[:,:].plot(kind='bar', width=0.8, color=color2)
plt.xticks(rotation=45)
plt.title('Arable land (% of land area)')
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.savefig('Barplot Arable land.png', bbox_inches='tight')
plt.show()

# 4th plot: Renewable Energy
plt.figure()
df_Renewable_energy.T.iloc[:,:].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Renewable energy consumption(% of total final energy consumption)')
plt.savefig('Barplot Renewable Energy.png', bbox_inches='tight')
plt.show();

# 5th plot: GDP Growth
plt.figure()
df_GDP.T.iloc[:,:].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('GDP growth (annual %)')
plt.savefig('Barplot GDP growth.png', bbox_inches='tight')
plt.show();

#6th plot: Forest Area
plt.figure()
df_Forest_Area.T.iloc[:,:].plot(kind='bar', width=0.8)
plt.xticks(rotation=60)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))
plt.title('Forest area (% of land area)')
plt.savefig('Barplot Forest Area.png', bbox_inches='tight')
plt.show();



