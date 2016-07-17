# coding: utf-8

import csv
from time import *
import evaluate_xml

def evaluate_taxi():
    node,way,relation,node1,graph,idx,lonlatid=evaluate_xml.evaluatexml()
    class Taxi :
        def __init__(self , lon = 0.0,lat = 0.0,status = 0,speed = 0,id = 0):
            self.lon = lon
            self.lat = lat
            self.status = status
            self.speed = speed
            self.id = id
    print "Begin evaluating taxis ..."
    time0 =time()
    idnum = {}
    taxi = []
    #idnum = {"line[0]" : num}
    #taxi = [[Taxi,Taxi,Taxi...],[...],...]

    csvfile = file('shanghai_taxi_20150401.csv', 'rb')
    reader = csv.reader(csvfile)
    flag = 0
    for line in reader:
        if flag == 0 :
            n = len(idnum)
            idnum[line[0]] = n
            #print idnum
            taxi.append([])
            flag = 1
        #if idnum.has_key(line[0]) == False :
        if line == [] :
            flag = 0
        else :
            num = idnum.get(str(line[0]))
            taxi[num].append(Taxi(line[3],line[4],line[5],line[9],line[0]))

    csvfile.close()
    time1 = time()
    print "End evaluating : %f" ,(time1 - time0)
    return taxi,idnum,node,way,relation,node1,graph,idx,lonlatid