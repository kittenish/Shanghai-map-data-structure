import sys
from xml.etree import ElementTree as ET
import cal_distance
from rtree import index
from time import *



def evaluatexml() :

    idx = index.Index()

    class Node :
        def __init__(self , id=0, lon = 0.0,lat = 0.0,name = "",nextnode = {},tags={},wayon = 0 ):
            self.id=id
            self.lon=lon
            self.lat=lat
            self.name=name
            self.nextnode={} #nextnode = {"id" : "distance"}
            self.waynum=[]
            self.tags=tags
            self.wayon = 0

    class Way:
        def __init__(self , ref = [],id = 0,name = "",tags = {}):
            self.ref = ref
            self.id = id
            self.name = name
            self.tags = tags

    print "Loading Shanghai_map ..."
    time0 = time()
    try:
        tree = ET.parse("shanghai_map.xml")
        root = tree.getroot()
    except Exception, e:
        print "Error:cannot parse file."
        sys.exit(1)
    time1 = time()
    print "Finaly open :%f" %(time1-time0)
    print "Start evaluating ..."
    time0=time()

    node = []
    way = []
    relation = []
    node1 = {}
    graph = {}
    lonlatid = {}
    idx = index.Index()

    for item in root :
        if item.tag == "node" :
            name  = ""
            tags={}
            for child in item.getchildren() :
                if(child.get("k") == "name") :
                    name = child.get("v")
                if child.tag == "tag":
                    tags[child.attrib['k']] = child.attrib['v']
            node.append(Node(item.get("id"),float(item.get("lon")),float(item.get("lat")),name,{},tags))
            idx.insert(int(item.get("id")),(float(item.get("lat")),float(item.get("lon"))),obj=True)
            n = len(node1)
            node1[item.get("id")] = n
            lonlatid[str(item.get("lon"))+str(item.get("lat"))] = item.get("id")


        elif item.tag == "way" :

            nums = []
            ref = []
            tags = {}
            for child in item.getchildren() :
                if child.tag == "nd" :
                    ref.append(child.get("ref"))
                    num = node1.get(child.get("ref"))
                    nums.append(num)
                elif child.tag == "tag":
                    tags[child.attrib['k']] = child.attrib['v']
            if tags.has_key("name") :
                way.append(Way(ref,item.get("id"),tags.get("name"),tags))
            else :
                way.append(Way(ref,item.get("id"),"",tags))
            des = len(ref)
            for i in xrange(0,des-1) :
                node[int(nums[i])].nextnode[ref[i+1]]=cal_distance.calcdistance(node[int(nums[i])].lat,node[int(nums[i])].lon,node[int(nums[i+1])].lat,node[int(nums[i+1])].lon)
                if tags.has_key("name") :
                    node[int(nums[i])].waynum.append(tags.get("name"))
                    #print node[int(nums[i])].waynum
            if tags.has_key("oneway") == False :
                for i in xrange(1,des) :
                    node[int(nums[i])].nextnode[ref[i-1]]=cal_distance.calcdistance(node[int(nums[i])].lat,node[int(nums[i])].lon,node[int(nums[i-1])].lat,node[int(nums[i-1])].lon)
            if tags.has_key("highway") or tags.has_key("bridge"):
                for i in xrange(des) :
                    node[int(nums[i])].wayon = 1

    for i in range(0,len(node)) :
        graph[node[i].id]=node[i].nextnode
        #graph {"node[i].id" : ["id" : "distance" , "id" : "distance"]}

    time1 = time()
    print "End eavluating : %f" %(time1-time0)
    return node,way,relation,node1,graph,idx,lonlatid
