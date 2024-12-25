#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:08:28 2024
@author: charlottelloyd
"""

import pandas as pd
import os

os.chdir('your/dir/here')

##############################################################################

zips = pd.read_excel('nc_zips.xlsx')
print('\nVerifying there are %s counties in NC.\n' % len(zips['County'].unique()))
zips['Zip5'] = zips['Zip'].astype('str')

orgs = pd.read_excel('nc_charitable_orgs.xlsx')
print('\nThere are %s orgs in the data.\n' % len(orgs))
orgs['Zip5'] = orgs['Zip'].str[:5]

orgs = pd.merge(orgs, zips[['Zip5','Zip_Type','County']], how='left', on='Zip5')
orgs.drop(columns='Zip5').to_excel('nc_charitable_orgs2.xlsx',index=False)