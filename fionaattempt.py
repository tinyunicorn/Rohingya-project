# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:18:41 2018

@author: Emma
"""

import pandas as pd

import geopandas as gpd
#from geopandas import GeoSeries, GeoDataFrame

#import urllib

#import json
#import geojson

#from shapely.geometry import Point

#import numpy as np

#import pyproj

#import shapely.wkt

import requests

import fiona

#import seaborn as sns

#import osmnx as ox

#import contextily as ctx

#import matplotlib.pyplot as plt
#import mplleaflet
#from mpl_toolkits.basemap import Basemap

#import folium
#from folium import FeatureGroup, LayerControl, Map, Marker
#from folium.plugins import HeatMap


#Get dataset with polygons, so we van calculate areas
link = 'https://services5.arcgis.com/QYf5PkPqzJKVzrmF/arcgis/rest/services/Rohingya_Refugee_Camps_Sites_Outline_May_18/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token='
request = requests.get(link)
b = bytes(request.content)
with fiona.BytesCollection(b) as f:
    crs = f.crs
    data_polygons = gpd.GeoDataFrame.from_features(f, crs=crs)

    
#Give both datasets the same name
data_polygons = data_polygons.rename(columns={'New_Camp_N': 'New_Camp_Name'})

print(data_polygons)

#Get dataset with populations
link = 'https://services5.arcgis.com/QYf5PkPqzJKVzrmF/arcgis/rest/services/Latest_Location_Masterlist_June_2018/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token='
request = requests.get(link)
b = bytes(request.content)
with fiona.BytesCollection(b) as f:
    crs = f.crs
    data_pop = gpd.GeoDataFrame.from_features(f, crs=crs)
    
link = 'https://services5.arcgis.com/QYf5PkPqzJKVzrmF/arcgis/rest/services/Latest_Location_Masterlist_June_2018/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token='
request = requests.get(link)
b = bytes(request.content)
with fiona.BytesCollection(b) as f:
    crs = f.crs
    data_pop = gpd.GeoDataFrame.from_features(f, crs=crs)
