from fcntl import DN_DELETE
import ee
from ee_plugin import  Map
import folium
import numpy as np
import rasterio
from rasterio.plot import reshape_as_raster

departamento_boqueron = ee.FeatureCollection("users/paofigue/Departamento_Boqueron")
filadelfia=ee.FeatureCollection('users/paofigue/filadelfia')
imageCollection = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
imageCollection2 = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
imageVisParam = {"opacity":1,"bands":["B5","B4","B3"],"min":7167.28,"max":15820.72,"gamma":1.6}
imageVisParam2 = {"opacity":1,"bands":["B4","B3","B2"],"min":6754.62,"max":18064.38,"gamma":1.6}
imageVisParam3 = {"opacity":1,"bands":["B8"],"min":7167.28,"max":15820.72,"gamma":1.6}


limite = filadelfia
Map.addLayer(limite, imageVisParam,'Limite')
Map.setCenter(-61.182, -21.96)

dataset_2016 = ee.ImageCollection(imageCollection2).filterDate('2016-06-01','2016-10-31').filterBounds(filadelfia).filter(ee.Filter.lte('CLOUD_COVER',10));#filtra lo que tiene 10% de nubosidad
dataset_2015 = ee.ImageCollection(imageCollection2).filterDate('2015-06-01','2015-08-30').filterBounds(filadelfia).filter(ee.Filter.lte('CLOUD_COVER',5)); #filtra lo que tiene 5% de nubosidad
composite_2016 = dataset_2016.median().clip(filadelfia).select(['B4', 'B3', 'B2'])
composite_2015 = dataset_2015.median().clip(filadelfia).select(['B8'])

Map.addLayer(composite_2016, imageVisParam2 , 'Mosaico_2016');
Map.addLayer(composite_2015, imageVisParam3 , 'Mosaico_2015');

# Select the corresponding bands for the multiespectral and panchromatic image
img_multi = dataset_2016.select(['B4', 'B3', 'B2'])
img_pan = dataset_2016.select(['B8'])

# Display the images on the map
#Map.addLayer(img_multi)
#Map.addLayer(img_pan)