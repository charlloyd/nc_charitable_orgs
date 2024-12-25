#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:28:39 2024
@author: charlottelloyd
"""

import pandas as pd
import pymupdf
import requests as re

os.chdir('your/dir/here')

##############################################################################
### Set up document 

response = re.get('https://www.sosnc.gov/imaging/dime/webportal/81219165.pdf')
content = response.content
doc = pymupdf.Document(stream=content)

##############################################################################
### scrape Section 2 table

col_names2 = ['License','Name','Address','City','State','Zip','Phone','Expiration']
data2 = pd.DataFrame(columns=col_names2)

for i in range(97,447):
    print('\nPage %s' % i)
    page = doc[i] 
    tabs = page.find_tables(horizontal_strategy="text", vertical_strategy="text")
    print(f"{len(tabs.tables)} table(s) on {page}")
    tab = tabs[0]
    df = tab.to_pandas()
    
    if df.columns[0] == 'Col0':
        header_row = df.index[df['Col0']=='License'].tolist()[0]
        df.columns = df.loc[header_row]
        df = df[header_row+1:]
        
    df['Name'] = df.iloc[:, df.columns.get_indexer_for(['Name'])[0]:df.columns.get_indexer_for(['Address'])[0]].apply(''.join,axis=1)
    df['Address'] = df.iloc[:, df.columns.get_indexer_for(['Address'])[0]:df.columns.get_indexer_for(['City'])[0]].apply(''.join,axis=1)
    
    df = df[col_names2]
    df = df[df['License']!='']
        
    data2 = pd.concat([data2,df])

##############################################################################
### scrape Section 3 table

col_names3 = ['License','Exempt. No.','Name','Address','City','State','Zip','Phone']
data3 = pd.DataFrame(columns=col_names3)

for i in range(450,529):
    print('\nPage %s' % i)
    page = doc[i] 
    tabs = page.find_tables(horizontal_strategy="text", vertical_strategy="text")
    print(f"{len(tabs.tables)} table(s) on {page}")
    tab = tabs[0]
    df = tab.to_pandas()
    
    if df.columns[0] == 'Col0':
        header_row = df.index[df['Col0']=='License'].tolist()[0]
        df.columns = df.loc[header_row]
        df = df[header_row+1:]
        
    df['Name'] = df.iloc[:, df.columns.get_indexer_for(['Name'])[0]:df.columns.get_indexer_for(['Address'])[0]].apply(''.join,axis=1)
    df['Address'] = df.iloc[:, df.columns.get_indexer_for(['Address'])[0]:df.columns.get_indexer_for(['City'])[0]].apply(''.join,axis=1)
    df['Phone'] = df.iloc[:, df.columns.get_indexer_for(['Phone'])[0]:].apply(''.join,axis=1)
    
    df = df[col_names3]
    df = df[df['License']!='']
        
    data3 = pd.concat([data3,df])

##############################################################################

data = pd.concat([data2,data3.rename(columns={'Exempt. No.':'Expiration'})])
data.to_excel('nc_charitable_orgs.xlsx', index=False)