#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:30:46 2017

@author: antonia
"""

digital = pd.read_csv('WB_Data_Digital.csv')
countries = pd.read_csv('List of countries.csv', )
digital = digital[digital['country'].isin(countries['Economy'])]
digital = digital[digital['date'] > 1991]

for x in list(digital.columns)[2:]:
    digital = clean_all_na(digital, 'country', x)
digital['Fixed broadband %'] *= 100
digital_1996 = digital[digital['date'] >= 1996]
mi = digital_1996.set_index(['date', 'country'])
midf = clean_nan(mi)
