def point_information (node,way,relation,node1,graph,idx,lonlatid) :
    id = ""
    while 1 :
        x= raw_input("Which kind of input do you prefer ? (id or position) : ")
        if x== "id" :
            y = str(input("Please input the id of the point : "))
            point = y
            break
        elif x=="position" :
            lon = input("Please input the lon of the point : ")
            lat = input("Please input the lat of the point : ")
            point = str(lonlatid.get(str(lon)+str(lat)))
            break
        else :
            print "Please input the correct type."
    print "id : ",node[node1.get(point)].id
    print "lon : ",node[node1.get(point)].lon
    print "lat : ",node[node1.get(point)].lat
    print "name : ",node[node1.get(point)].name
    print "nextnode : ",node[node1.get(point)].nextnode
    print "tags : ",node[node1.get(point)].tags
    print "wayon : ",node[node1.get(point)].wayon