import math
import copy

#graph creation setttings
friendD = 10
angleTolerance = math.pi/8
calLength = 4

def distanceTwoPoints(P, Q):
    return (((P[0]-Q[0])**2 + (P[1]-Q[1])**2)**(1/2))

def insertList(L, element, elementIndex):
    length = len(L[0])

    for i in range(length-1, 0, -1):
        if L[1][i-1] < element < L[1][i]:
            L[0].insert(i, elementIndex)
            L[1].insert(i, element)
            break

    if element < L[1][0]:
            L[0].insert(0, elementIndex)
            L[1].insert(0, element)

    return [L[0][0:length], L[1][0:length]]

def makeAngle(dy, dx):
    try:
        angle = math.atan(dy/dx)
        return angle
    except:
        return math.pi/2

def weightAngles(angles, tolerance):
    adj = [[angles[0][0], angles[0][1], angles[0][2]]]
    for i in range(len(angles)):
        grouped = False
        for j in range(len(adj)):
            if abs(angles[i][1] - adj[j][1]) < (tolerance):
                grouped = True
                
                #assign the closer
                if adj[j][2] < angles[i][2]:
                    adj[j] = angles[i]

        if not grouped:
            adj.append(angles[i])
            
                

    return adj
            
def makeGraph(nodes, friendD, angleTolerance, calLength):
    # nodesFile = open('nodes.txt', 'r')
    # nodes = nodesFile.read().split("\n")
    # nodesFile.close()

    # for i in range(len(nodes)):
    #     nodes[i] = nodes[i][1:-1]
    #     nodes[i] = nodes[i].split(".")
    #     nodes[i][0] = int(nodes[i][0])
    #     nodes[i][1] = int(nodes[i][1])
    #     if len(nodes[i]) > 2:
    #         nodes[i] = [nodes[i][0], nodes[i][1]]

    # print (nodes)
    #proper list of nodes

    graph = [[]]*len(nodes)

    graphrow = [9999]*len(nodes)

    for i in range(len(nodes)):
        graph[i] = copy.deepcopy(graphrow)
    ##what the fuck why is aliasing a thing this shit took like an hour to debug

    '''
    output = open('pregraph.txt', "a")

    for i in range(len(graph)):
        output.write("[")
        for j in range(len(graph[i])):
            output.write(str(graph[i][j]))
            if j != len(graph[i]):
                output.write(", ")
        output.write("]\n")

    output.close()
    '''

    for i in range(len(nodes)):

        closestFour = [["A"]*calLength, [9999]*calLength]
        closestNodes = [[], []]
        
        for j in range(len(nodes)):
            distances = distanceTwoPoints(nodes[i], nodes[j])
            if i != j:
                distances = distanceTwoPoints(nodes[i], nodes[j])
                #print(distances)
                if distances < friendD:
                    closestNodes[0].append(j)
                    closestNodes[1].append(distances)
                
            #print (i, j, distances)
        
        for j in range(len(nodes)):
            distances = distanceTwoPoints(nodes[i], nodes[j])
            if i != j and (distances not in closestNodes[0]):
                closestFour = insertList(closestFour, distances, j)


        angles = []
        listAdj = []
        #angles = [[index, angle, distance]]
        
        #print(closestNodes, closestFour)

        for k in range(len(closestNodes[0])):
            dx = nodes[i][0] - nodes[closestNodes[0][k]][0]
            dy = nodes[i][1] - nodes[closestNodes[0][k]][1]
            angles.append([closestNodes[0][k], makeAngle(dy, dx), distanceTwoPoints(nodes[i], nodes[closestNodes[0][k]])])

        for k in range(calLength):
            dx = nodes[i][0] - nodes[closestFour[0][k]][0]
            dy = nodes[i][1] - nodes[closestFour[0][k]][1]
            angles.append([closestFour[0][k], makeAngle(dy, dx), distanceTwoPoints(nodes[i], nodes[closestFour[0][k]])])

        listAdj = weightAngles(angles, angleTolerance)
        #print(listAdj)


        #add adjacency to that node for the graph
        #adjList = [[index, angle, distance]]  (same as angles)
        for j in range(len(listAdj)):
            graph[i][listAdj[j][0]] = listAdj[j][2]
            graph[listAdj[j][0]][i] = listAdj[j][2]


    #print(graph[0])

    output = open('graph.txt', "a")

    for i in range(len(graph)):
        output.write("[")
        for j in range(len(graph[i])):
            output.write(str(graph[i][j]))
            if j != len(graph[i]):
                output.write(", ")
        output.write("]\n")

    output.close()

    return graph



#weighted average stuff, not useful >:(

'''
intervals = [0]*8

for i in range(len(angles)):
    if angles[i] < 0:
        angles[i] += math.pi

    red = angles[i]

    val = 8
    while red >= 0:
        red -= math.pi/8
        val -= 1

    intervals[val] += 1

#finding the common slopes
peaks = []
prevM = intervals[0] - intervals[7]
for i in range(len(intervals) - 1):
    curM = intervals[i+1] - intervals[i]

    if prevM > 0 and curM < 0:
        peaks.append(i)

    prevM = curM

curM = intervals[0] - intervals[7]

if prevM > 0 and curM < 0:
    peaks.append(7)

#peaks is probably 2 indices

m1=((angles[peaks[0]-1]*(peaks[0]-1)*math.pi/8) + (angles[peaks[0]]*(peaks[0])*math.pi/8) + (angles[peaks[0]+1]*(peaks[0]+1)*math.pi/8))/(angles[peaks[0]-1] + angles[peaks[0]] + angles[peaks[0]+1])
m2=((angles[peaks[1]-1]*(peaks[1]-1)*math.pi/8) + (angles[peaks[1]]*(peaks[1])*math.pi/8) + (angles[peaks[1]+1]*(peaks[1]+1)*math.pi/8))/(angles[peaks[1]-1] + angles[peaks[1]] + angles[peaks[1]+1])

weightedM = [m1, m2]

'''
