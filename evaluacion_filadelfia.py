import ee
from ee_plugin import  Map

ee.Initialize()
# imagenLC8 = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_007059_20170814')
# visparam = {'min':0, 'max':0.4, 'bands':['B6','B5','B4']}
# Map.addLayer(imagenLC8,visparam,'LC8654')
# Map.centerObject(imagenLC8,9)

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
Map.addLayer(limite)
Map.setCenter(-61.182, -21.96)

# point_bosque_1=ee.Geometry.Point([-60.371259413088225,-20.602807874701703])
# print(point_bosque_1)



print('fin')