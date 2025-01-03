#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:02:32 2024
@author: charlottelloyd
"""

import os
from geojson import Feature, FeatureCollection, Point
import pandas as pd
 
os.chdir('your/dir/here')

features = []

df = pd.read_excel('BMF_NC2.xlsx')

for idx, row in df.iterrows():
    features.append(Feature(geometry = Point((float(row.LONGITUDE), float(row.LATITUDE))), 
                            properties = {'established': row.ORG_YEAR_FIRST,
                                          'last_active': row.ORG_YEAR_LAST,
                                          'tooltip': '%s (est. %s)' % (row.ORG_NAME_CURRENT,row.ORG_YEAR_FIRST)}))

collection = FeatureCollection(features)
with open("BMF_NC2.json", "w") as f:
    f.write('%s' % collection)