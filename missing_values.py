#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:34:56 2017

@author: antonia
"""

import numpy as np

def clean_all_na(df, key, var):
    """This function takes in a dataframe, a key i.e. column vector, by whcih to groupby
    and a variable. It returns a dataframe that has all the values in key
    that do not have any values for variable var removed.
    """
    grouped = df.groupby(key, as_index = False).mean()
    grouped_na = grouped[grouped[var].isnull()]
    df = df[~df[key].isin(grouped_na[key])]
    return df

def clean_nan(df):
    '''This function takes in a tidy dataframe.
    It returns a new dataframe cleaned in the following way: 
        If there are no values for this country up to this year, it
        imputes a 0.
        If the nan-value is in-between known values, 
        it imputes the mean.'''
        
    for var in list(df.columns[2:]):
        for country in list(df.country.unique()):
            time = min(set(list(df['date'])))
            condition = np.nan(
                    df[df['date']==time and df['country']==country][var])
            while condition:
                df[df['date']==time and df['country']==country][var] = 0
                time += 1
                condition = np.nan(
                        df[df['date']==time and df['country']==country][var])
        return df