#-*-coding:utf-8-*-
from mapnik import *
import PyQt4
mapfile = 'mapnik_style.xml'
map_output = 'mymap.png'

m = Map(16*1024,16*1024)
load_map(m,mapfile)
bbox = (Box2d(121,30.8,122, 31.5))
m.zoom_to_box(bbox)
print "Scale = ",m.scale()
render_to_file(m,map_output)