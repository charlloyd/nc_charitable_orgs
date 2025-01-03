# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html
import geojson

import os

os.chdir('/Users/charlottelloyd/Documents/Projects/git/nc_charitable_orgs')

with open('BMF_NC2.json') as f:
    gj = geojson.load(f)

app = Dash()
app.layout = html.Div([
    dl.Map([dl.TileLayer(),
            dl.GeoJSON(data = gj, cluster=True, zoomToBoundsOnClick=True,
                       superClusterOptions={"radius": 100})], 
                       center=(35, -79), zoom=7, style={'height': '50vh'})])

if __name__ == '__main__':
    app.run_server()