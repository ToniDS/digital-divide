#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:09:16 2017

@author: antonia
"""

#__all__['clean_nan', 'clean_nan2', 'clean_all_na']


import pandas as pd
import numpy as np

def clean_nan(midf, variables):
    '''This function takes in a multi-index dataframe with indices
    date and country and the variables I wish to check. 
    Vars need to have float values.
    It returns a new dataframe cleaned in the following way: 
        If there are no values for this country up to this year, it
        imputes a 0.
        If the nan-value is in-between known values, 
        it imputes the mean.'''
        
    
    #create sets that store the countries and years
    countries = list(set([x for (x,y) in midf.index.values]))
    years = list(set([y for (x,y) in midf.index.values]))
    
    
    types = []
    #Firstly, replace all leading NaNs with 0
    for country in countries:
        for var in variables:
            time = min(years)
            condition = midf.loc[(country, time), var]
            while np.isnan(condition) and time <= max(years):
                midf.loc[(country, time), var] = 0
                time = time + 1
                condition = midf.loc[(country, time), var]
    
            
            ###secondly, where possible, replace values with mean of preceding and following values
    for country in countries:
        for var in variables:
            for time in years:
                condition = midf.loc[(country, time), var]
                if np.isnan(condition) and (min(years) < time < max(years)):
                    aver = (midf.loc[(country, time-1), var] + midf.loc[(
                            country, time+1), var]) /2
                    midf.loc[(country, time), var] = aver
                    
                
    return midf


def clean_all_na(df, key, var):
    """This function takes in a dataframe, a key i.e. column vector, by which to group
    and a variable. It returns a dataframe that has all the values in key
    that do not have any values for variable var removed.
    """
    grouped = df.groupby(key, as_index = False).mean()
    grouped_na = grouped[grouped[var].isnull()]
    df = df[~df[key].isin(grouped_na[key])]
    return df


