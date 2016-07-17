import heapq
from time import *

def dijkstra_score(shortest_distances, v, w,graph):
    return shortest_distances[v] + graph.get(str(v)).get(str(w))

short_way = {}
heap = []
pre = {} #{"id" : "preid"}
preid = {}
#help(heapq)
def dijkstra(source,destination_vertices,graph):
    unprocessed = set(graph.keys()) # vertices whose shortest paths from source have not yet been calculated
    #print('3537063830' in unprocessed)
    unprocessed.remove(str(source))
    shortest_distances = {str(source): 0}
    if graph.has_key(str(source))==False :
        return
    n = 0
    find = {} #{ dis : n }
    disidtemp = []
    disid = {} #{ dis : id }

    #for head in graph.get(str(source)):
        #dis = dijkstra_score(shortest_distances, str(source), head,graph)
        #heapq.heappush(heap,dis)
        #disid[dis] = head
        #short_way[head] = str(source)
    #sh = heapq.heappop(heap)
    #closest_head = disid.get(sh)
    #del disid[sh]
    #shortest_distances[str(closest_head)] = sh
    #unprocessed.remove(str(closest_head))

    #for i in xrange(len(graph) - 1):
        # find a vertex with the next shortest path, i.e. minimal Dijkstra score
        #m = float('inf')
        #closest_head = 0
        #for tail in shortest_distances :
            #for head in graph.get(str(tail)):
                #if head in unprocessed:
                    #print head
                    #d = dijkstra_score(shortest_distances, tail, head, graph)
                    #if d < m:
                        #m=d
                        #closest_head = head
                        #short_way[closest_head] = tail
    closest_head = source

    for i in xrange(len(graph) - 1):
        for head in graph.get(str(closest_head)):
            dis = dijkstra_score(shortest_distances, str(closest_head), head, graph)
            heapq.heappush(heap,dis)
            if disid.has_key(dis) == False :
                disid[dis] = head
                preid[head] = closest_head
            else :
                if find.has_key(dis) == False :
                    find[dis] = n
                    disidtemp.append([])
                    #print disidtemp
                    disidtemp[n].append(head)
                    disidtemp[n].append(closest_head)
                    #print disidtemp
                    n = n+1
                else :
                    disidtemp[find.get(dis)].append(head)
                    disidtemp[find.get(dis)].append(closest_head)

        prepoint = closest_head
        temp = closest_head
        while 1:
            if heap != []:
                sh = heapq.heappop(heap)
            else :
                break
            temp = disid.get(sh)
            prepoint = preid.get(temp)
            if temp in unprocessed :
                #print temp
                break
            if find.has_key(sh) :
                flag = 0
                position = find.get(sh)
                leng = len(disidtemp[position])
                if leng!=0 :
                    for j in xrange(0,leng) :
                        if j%2 == 0:
                            if heap!=[] :
                                heapq.heappop(heap)
                            if disidtemp[position][j] in unprocessed:
                                temp = disidtemp[position][j]
                                #print leng,j
                                #if leng ==1:
                                    #print disidtemp[position]
                                prepoint = disidtemp[position][j+1]
                                flag = 1
                                if j!=leng-2 :
                                    disid[sh] = disidtemp[position][j+2]
                                    preid[disid[sh]] = disidtemp[position][j+3]
                                    for x in xrange(0,j+4) :
                                        del disidtemp[position][x]
                                else :
                                    #print sh
                                    disidtemp[position] = []
                                    del disid[sh]
                                break
                if flag == 1 :
                    #print sh
                    break
                else :
                    disidtemp[position] = []
                    del disid[sh]

        if temp in unprocessed :
            #print closest_head,sh
            #print temp
            short_way[temp] = str(closest_head)
            pre[temp] = prepoint
            closest_head = temp
            unprocessed.remove(str(closest_head))
            shortest_distances[str(closest_head)] = sh
            if temp == str(destination_vertices) :
                break
        #if find.has_key(sh) :
         #   position = find.get(sh)
          #  leng = len(disidtemp[position])
           # if leng == 1 :
            #    disid[sh] = disidtemp[position][0]
             #   disidtemp[position] = []
            #else :
             #   disid[sh] = disidtemp[position][0]
              #  del disidtemp[position][0]

    # in case G is not fully connected
    for vertex in unprocessed:
        shortest_distances[vertex] = float('inf')

    return shortest_distances


def fshortest_path(node,way,relation,node1,graph,idx,lonlatid) :

    source = int(input("Enter source vertex: "))
    destination_vertices = int(input("Destination vertices:"))
    print "Begin to calculate ..."
    time0=time()
    if source != destination_vertices :
        flag = {}
        n = 1
        ans = 0
        if node[node1.get(str(source))].wayon == 0 :
            while 1 :
                flag[str(source)] = "yes"
                newsource = idx.nearest((node[node1.get(str(source))].lat,node[node1.get(str(source))].lon), n*10, objects=True)
                for i in newsource:
                    #print i
                    if flag.has_key(str(i.id)) :
                            continue
                    j = node1.get(str(i.id))
                    flag[str(i.id)] = "yes"
                    if node[j].wayon ==1 :
                        source = int(i.id)
                        ans = 1
                        break
                if ans == 1 :
                    break
                n = n+1

            print "Change source to the nearest point : %d" %int(source)

        flag = {}
        n = 1
        ans = 0
        if node[node1.get(str(destination_vertices))].wayon == 0 :
            while 1 :
                flag[str(destination_vertices)] = "yes"
                newdes = idx.nearest((node[node1.get(str(destination_vertices))].lat,node[node1.get(str(destination_vertices))].lon), n, objects=True)
                for i in newdes:
                    #print i
                    if flag.has_key(str(i.id)) :
                            continue
                    j = node1.get(str(i.id))
                    flag[str(i.id)] = "yes"
                    if node[j].wayon == 1 :
                        destination_vertices = int(i.id)
                        ans = 1
                        break
                if ans == 1 :
                    break
                n = n+1
            print "Change destination to the nearest point : %d" %int(destination_vertices)
        distances = dijkstra(source,destination_vertices,graph)
        d = distances[str(destination_vertices)]
    else :
        d = 0.000000
    time1=time()
    print "The distance from %d to vertex %d is : %f." % (source, destination_vertices, d)
    print "Using time : %f" %(time1-time0)
    if d!= float('inf') :
        waypoint =[]
        i=str(destination_vertices)
        waypoint.append(i)

        while i != str(source) :
        #print i
            i = str(pre.get(i))
            waypoint.append(i)
        print "Here is the shortest way : "
        print waypoint[::-1]



