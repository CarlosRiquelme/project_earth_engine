from fcntl import DN_DELETE
import ee
from ee_plugin import  Map
import folium
# from map_display import Mapdisplay


#ee.Initialize()
# imagenLC8 = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_007059_20170814')
# visparam = {'min':0, 'max':0.4, 'bands':['B6','B5','B4']}
# Map.addLayer(imagenLC8,visparam,'LC8654')
# Map.centerObject(imagenLC8,9)


def cloudMaskL457 (image):
    qa = image.select('BQA')
    cloud1 = qa.bitwiseAnd(1 << 8).eq(0)
    cloud2 =qa.bitwiseAnd(1 << 75).eq(0)
    cloud3 =qa.bitwiseAnd(1 << 3).eq(0)
    mask2 = image.mask().reduce(ee.Reducer.min())
    return image.updateMask(cloud1).updateMask(cloud2).updateMask(cloud3).updateMask(mask2).divide(10000).copyProperties(image, ["system:time_start"])


Departamento_boqueron = ee.FeatureCollection("users/paofigue/Departamento_Boqueron")
filadelfia=ee.FeatureCollection('users/paofigue/filadelfia')
imageCollection = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
imageCollection2 = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
imageVisParam = {"opacity":1,"bands":["B5","B4","B3"],"min":7167.28,"max":15820.72,"gamma":1.6}
imageVisParam2 = {"opacity":1,"bands":["B5","B4","B3"],"min":6754.62,"max":18064.38,"gamma":1.6}
imageVisParam3 = {"opacity":1,"bands":["B4","B5","B6"],"min":7167.28,"max":15820.72,"gamma":1.6}
# bosque = geometry2,
# cambios = geometry3,
# no_bosque =geometry;

limite = filadelfia
Map.addLayer(limite, imageVisParam,'Limite')
Map.setCenter(-61.182, -21.96)


point_bosque_1=ee.Geometry.Point([-60.371259413088225,-20.602807874701703])
# poly1 = ee.Geometry.Point([-50, 30]).buffer(1e6)
# print(poly1)
# Mapdisplay(center= (30,-45),dicc={'point':point_bosque_1},zoom_start=3)
dataset_2016 = ee.ImageCollection(imageCollection2).filterDate('2016-06-01','2016-10-31').filterBounds(filadelfia).filter(ee.Filter.lte('CLOUD_COVER',10));#filtra lo que tiene 10% de nubosidad
dataset_2015 = ee.ImageCollection(imageCollection2).filterDate('2015-06-01','2015-08-30').filterBounds(filadelfia).filter(ee.Filter.lte('CLOUD_COVER',5)); #filtra lo que tiene 5% de nubosidad
composite_2016 = dataset_2016.median().clip(filadelfia).select("B[2-9]*")
composite_2015 = dataset_2015.median().clip(filadelfia).select("B[2-9]*")

#map(cloudMaskL457)


visParam={
    'bands': ['B4','B3','B2'],
    'min': 211.2,
    'max':1196.8,
    'gamma':1.6
}

Map.addLayer(composite_2016, imageVisParam2 , 'Mosaico_2016');
Map.addLayer(composite_2015, imageVisParam3 , 'Mosaico_2015');

mosaicmf= composite_2016.addBands(composite_2015);
Map.addLayer(mosaicmf, imageVisParam , 'Mosaico_15-16');

##normalizacion 

#clasificacion supervisada


#print(dataset_2016)
print('fin')

