# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:21:33 2023

@author: MARYANN
"""

# importing necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# writing a function for used in reading the data

def read_file(file_path, index_column):
    # Read the file into a DataFrame
    df = pd.read_excel(file_path)

    # Set the specified column as the index
    df.set_index(index_column, inplace=True)

    # Transpose the DataFrame
    df_country = df.T

    # Drop columns with all null values
    df_country.dropna(axis=1, how='all', inplace=True)
    
    # call the variables to be returned
    return df, df_country

# defining the augments for the function to take
file_path = 'World_Development.xlsx'
index_column = ['Country Name','Series Name']

# using the defined function to read the data
output = read_file(file_path, index_column)

#
df = output[0]
df_country=output[1]

# checking the content of the data
print(df.head(5))
