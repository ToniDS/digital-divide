#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:09:16 2017

@author: antonia
"""

#__all__['clean_nan', 'clean_nan2', 'clean_all_na']


import pandas as pd
import numpy as np

def clean_nan(midf):
    '''This function takes in a multi-index dataframe with indices
    date and country.
    It returns a new dataframe cleaned in the following way: 
        If there are no values for this country up to this year, it
        imputes a 0.
        If the nan-value is in-between known values, 
        it imputes the mean.'''
        
    
    #create sets that store the countries and years
    countries = list(set([x for (y,x) in midf.index.values]))
    years = list(set([y for (y,x) in midf.index.values]))
    

    
    #Firstly, replace all leading NaNs with 0
    for var in midf.columns:
        for country in countries:
            time = min(years)
            condition = np.isnan(midf.loc[(time, country), var])
            while condition and time <= max(years):
                midf.loc[(time, country), var] = 0
                time += 1
                condition = np.isnan(midf.loc[(time, country), var])
                #This means there are no values in the entire country for var
                ##if time >= max(years):
                  #  return country, var
            
            #secondly, where possible, replace values with mean of preceding and following values
    for var in midf.columns:
        for country in countries:
            for time in years:
                condition = np.isnan(midf.loc[(time, country), var])
                if condition and (min(years) < time < max(years)):
                    aver = (midf.loc[(time-1, country), var] + midf.loc[(time+1, country), var]) /2
                    midf.loc[(time, country), var] = aver
    
                
    return midf

#This code does not work from spyder, but does work in the jupyter notebook. Why?

#secondly, where possible, replace values with mean of preceding and following values
#create sets that store the countries and years


def clean_all_na(df, key, var):
    """This function takes in a dataframe, a key i.e. column vector, by whcih to groupby
    and a variable. It returns a dataframe that has all the values in key
    that do not have any values for variable var removed.
    """
    grouped = df.groupby(key, as_index = False).mean()
    grouped_na = grouped[grouped[var].isnull()]
    df = df[~df[key].isin(grouped_na[key])]
    return df

