#-*-coding:utf-8-*-
import short_path_dijkstra
from time import *
import way_information
import place_nearby
import evaluate_taxi
import evaluate_xml
import point_information
import find_taxi

#taxi,idnum,node,way,relation,node1,graph,idx,lonlatid= evaluate_taxi.evaluate_taxi()
node,way,relation,node1,graph,idx,lonlatid=evaluate_xml.evaluatexml()
def main() :
    while 1 :
        print "Choose:\n\t1.shortest_path\n\t2.Road information\n\t3.Point information\n\t4.Places nearby\n\t5.Find taxis."
        x = input()
        if x==1 :
            short_path_dijkstra.fshortest_path(node, way, relation, node1, graph, idx, lonlatid)
        elif x==2 :
            way_information.way_information(node,way,relation,node1,graph,idx)
        elif x==3 :
            point_information.point_information(node,way,relation,node1,graph,idx,lonlatid)
        elif x==4 :
            place_nearby.places_nearby(node,way,relation,node1,graph,idx,lonlatid)
        #elif x==5 :
            #find_taxi.taxi_information(taxi,idnum,node,way,relation,node1,graph,idx,lonlatid)
        s = raw_input("Do you want to continue?(yes/others to represent no) ")
        if s!="yes" :
            break

main()
