#-*-coding:utf-8-*-
# -*- coding: gb18030 -*-
import evaluate_xml
import cal_distance

#node,way,relation,node1,graph,idx=evaluate_xml.evaluatexml()

def way_information(node,way,relation,node1,graph,idx) :
    wayinfor = []
    name =str(raw_input("Please input the road name : ".decode('utf-8').encode('gbk')))
    #print name
    name = unicode(name,'utf-8')
    for iway in way :
        if iway.name == name :
            wayinfor.append(iway.ref)

    lenofway = 0
    waypoint = []

    for iway in wayinfor :
        waypoint.append(iway[0])
        for i in xrange(1,len(iway)) :
            num1 =  node1.get(iway[i])
            num2 =  node1.get(iway[i-1])
            lenofway = lenofway + cal_distance.calcdistance(node[num1].lat,node[num1].lon,node[num2].lat,node[num2].lon)
            waypoint.append(iway[i])

    print "Do you want to print every node on the way?(yes/others to represent no)"
    request = raw_input()
    if request == "yes" :
        print waypoint

    print "The length of the road is %f"  %lenofway
    return wayinfor







