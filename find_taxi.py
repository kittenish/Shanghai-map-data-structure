def taxi_information(taxi,idnum,node,way,relation,node1,graph,idx,lonlatid):
    num = raw_input("Please input the No. of the taxi : ")
    pointsignal = raw_input("Do you want to show all the points on the way ? ")
    #print idnum
    no = idnum.get(str(num))
    #print no
    if no == None :
        print "Please input the correct number."
    else :
        leng = len(taxi[no])
        if pointsignal == "yes" :
            for i in taxi[no]:
                print "Lon : ",i.lon," ; lat : ",i.lat," ; status : ",i.status," ; speed : ",i.speed
        print "Total points on the way : %d" %leng
    return taxi[no]
