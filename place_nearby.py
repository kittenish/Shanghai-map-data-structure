#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def places_nearby(node,way,relation,node1,graph,idx,lonlatid) :
    x= raw_input("Which kind of input do you prefer ? (id or position) : ")
    id = ""
    while 1 :
        if x== "id" :
            y = str(input("Please input the id of the point : "))
            id = y
            break
        elif x=='position' :
            lon = input("Please input the lon of the point : ")
            lat = input("Please input the lat of the point : ")
            id = str(lonlatid.get(str(lon)+str(lat)))
            break
        else :
            print "Please input the correct type."

    while 1:
        x = raw_input("\t1. area search; \n\t2. nearest places ")
        if x == '1' :
            print "Please input the edge of the searching area : "
            numlon = float(raw_input("lon : "))
            numlat = float(raw_input("lat : "))
            lon1 = node[node1.get(id)].lon - numlon
            lon2 = node[node1.get(id)].lon + numlon
            lat1 = node[node1.get(id)].lat - numlat
            lat2 = node[node1.get(id)].lon + numlat
            nodetemp = idx.intersection((lat1,lon1 ,lat2,lon2 ), objects=True)
            signalway = raw_input("Do you want to display all the ways ? (yes or others to represent no)")
            signalpoint = raw_input("Do you want to display all the interesting points ? (yes or others to represent no)")
            #signaltexi = raw_input("Do you want to display all the taxis nearby ? (yes or others to represent no)")
            wayname = {}
            pointpoint = []
            waynumber = 0
            pointnumber = 0
            if signalway == "yes" :
                print "Here are the ways :"
            for i in nodetemp :
                j = node1.get(str(i.id))
                if signalpoint == "yes" :
                    if node[j].tags.has_key("aeroway",) or node[j].tags.has_key("railway") or node[j].tags.has_key( "highway") or node[j].tags.has_key("amenity" )or node[j].tags.has_key( "public_transport") or node[j].tags.has_key( "barrier") or  node[j].tags.has_key("power") or node[j].tags.has_key("place") or node[j].tags.has_key("tourism") or node[j].tags.has_key( "shop") or node[j].tags.has_key( "waterway") or node[j].tags.has_key( "leisure") or node[j].tags.has_key( "building") or node[j].tags.has_key( "historic") or node[j].tags.has_key("sport") or node[j].tags.has_key( "man_made") or node[j].tags.has_key("office") or node[j].tags.has_key( "natural") :
                        pointpoint.append(j)
                        pointnumber = pointnumber +1

                if signalway == "yes" :
                    if node[j].waynum != [] :
                        for name in node[j].waynum :
                            if wayname.has_key(name) == False :
                                wayname[name] = "yes"
                                print "\t",name
                                waynumber = waynumber+1
            if signalway == "yes" :
                print "TotaL ways : %d." %waynumber

            if signalpoint == "yes" :
                print "Here are the points :"
                for j in pointpoint:
                    print node[j].id," : ",node[j].lon ," ",node[j].lat
                    print "\t",node[j].tags
                print "Total points : %d." %pointnumber
            break

        elif x == '2':
            pointnum = raw_input("How many interested options are you looking for ? ")
            pointtype = raw_input("What type do you want to search ? (highway/shop/tourism/ ... /all)")
            print "Here are the points :"
            if pointtype == "all" :
                count = 0
                n = int(pointnum)
                flag = {}
                while count < int(pointnum) :
                    hits = idx.nearest((node[node1.get(str(id))].lat,node[node1.get(str(id))].lon), n, objects=True)
                    for i in hits :
                        if flag.has_key(str(i.id)) :
                            continue
                        j = node1.get(str(i.id))
                        if node[j].tags.has_key("aeroway",) or node[j].tags.has_key("railway") or node[j].tags.has_key( "highway") or node[j].tags.has_key("amenity" )or node[j].tags.has_key( "public_transport") or node[j].tags.has_key( "barrier") or  node[j].tags.has_key("power") or node[j].tags.has_key("place") or node[j].tags.has_key("tourism") or node[j].tags.has_key( "shop") or node[j].tags.has_key( "waterway") or node[j].tags.has_key( "leisure") or node[j].tags.has_key( "building") or node[j].tags.has_key( "historic") or node[j].tags.has_key("sport") or node[j].tags.has_key( "man_made") or node[j].tags.has_key("office") or node[j].tags.has_key( "natural") :
                            print node[j].id," : ",node[j].lon ," ",node[j].lat
                            print '\t',node[j].tags
                            flag[str(i.id)] = "yes"
                            count = count + 1
                    n = n + 1
            else :
                count = 0
                n = int(pointnum)
                flag = {}
                while count < int(pointnum) :
                    hits = idx.nearest((node[node1.get(str(id))].lat,node[node1.get(str(id))].lon), n, objects=True)
                    for i in hits :
                        if flag.has_key(str(i.id)) :
                            continue
                        j = node1.get(str(i.id))
                        if node[j].tags.has_key(pointtype) :
                            print node[j].id," : ",node[j].lon ," ",node[j].lat
                            print '\t',node[j].tags
                            flag[str(i.id)] = "yes"
                            count = count + 1
                    n = n + 1
            break
        else :
            print "Please choose the correct type."

