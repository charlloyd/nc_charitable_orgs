# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import dash_leaflet as dl
from dash import Dash, html
import geojson

with open('BMF_NC2.json') as f:
    gj = geojson.load(f)

app = Dash()
server = app.server

app.layout = html.Div([
    dl.Map([dl.TileLayer(),
            dl.GeoJSON(data = gj, cluster=True, zoomToBoundsOnClick=True,
                       superClusterOptions={"radius": 100})], 
                       center=(35, -79), zoom=7, style={'height': '50vh'})])

if __name__ == '__main__':
    app.run_server()
