import math
import graph
import random
import timeit

#function used to time algorithms
def time(com, mySetup):
     return timeit.timeit(com, number = 1, setup = mySetup)

#this generates a euclidean distance graph with a specified number of nodes
#and coordinates in a certain range
def generateEuclidGraph(numNodes, coord_range):
    f = open("testGraph.txt", "w+")
    numberOfNodes = random.randint(1,numNodes)
    for i in range(numberOfNodes):
        x_coord = random.randint(1,coord_range)
        y_coord = random.randint(1,coord_range)
        f.write("{} {}\n".format(x_coord, y_coord))
    f.close()
    mySetup = '\n'.join((
        'import graph',
        'g = graph.Graph(-1, "testGraph.txt")'
    ))
    print(time('g.swapHeuristic',  mySetup))
    print(time('g.TwoOptHeuristic', mySetup))
    print(time('g.Greedy', mySetup))
    print(time('g.nearestInsertion', mySetup))


#Because of time limitations on my part and not wanting to
#make my report too long I haven't included any results
#on Metric vs Non-Metric graphs. However I've left the code
#for generating a Metric Graph in.
def generateMetricGraph(numNodes, distance_range):
    f = open("testGraph2.txt", "w+")
    numberOfNodes = numNodes
    for i in range(numberOfNodes):
        #for a metric graph if the distance is in a range (a,b) such that
        #2a > b then it satisfies the triangle inequality
        distance = random.randint((distance_range/2 +1), distance_range)
        f.write("{} {} {}\n".format(i, ((i+ random.randint(1,numberOfNodes))%numberOfNodes), distance))

    f.close()



#the following function creates a planted solution where the graph is essentially a square
#with an optimal solution to be following the perimeter of the square

#for my other planted solution involving a rectangle I modified the function slightly
# so the 1st and 3rd for loops go up to numNodesQuart +2
#and the 2nd and 4th for loops go up to numNodesQuart -2
def plantedSoln(numNodes):
    if numNodes%4  != 0:
        return "cannot create square graph"
    f = open("plantedSoln.txt", "w+")
    numberOfNodes = numNodes
    numNodesQuart = numberOfNodes//4

    #creating coords for each side of sqaure
    for i in range(0, (numNodesQuart)):
        x_coord = i + 100
        y_coord = 100
        f.write("{} {}\n".format(x_coord, y_coord))
    for i in range(0, (numNodesQuart)):
        x_coord = numNodesQuart + 100
        y_coord = i + 100
        f.write("{} {}\n".format(x_coord, y_coord))
    for i in range(0,(numNodesQuart)):
        x_coord = numNodesQuart - i + 100
        y_coord = numNodesQuart + 100
        f.write("{} {}\n".format(x_coord, y_coord))
    for i in range(0, (numNodesQuart)):
        x_coord = 100
        y_coord = numNodesQuart - i + 100
        f.write("{} {}\n".format(x_coord, y_coord))
    f.close()

    g = graph.Graph(-1, "plantedSoln.txt")
    print(g.tourValue())
    #randomises the list so we don't start with the
    #optimal solution
    g.perm = random.sample(range(numNodes), numberOfNodes)

    #this part of the code isnt particuarly clean but it
    #prints out all the times for the planted solution
    mySetup = '\n'.join((
        'import graph',
        'g = graph.Graph(-1, "plantedSoln.txt")'
    ))
    print(time('g.swapHeuristic()', mySetup))
    g.swapHeuristic()
    print(g.tourValue())
    print('**********************************************')

    mySetup = '\n'.join((
        'import graph',
        'g = graph.Graph(-1, "plantedSoln.txt")'
    ))
    print(time('g.TwoOptHeuristic()', mySetup))
    g.TwoOptHeuristic()
    print(g.tourValue())
    print('**********************************************')

    mySetup = '\n'.join((
        'import graph',
        'g = graph.Graph(-1, "plantedSoln.txt")'
    ))
    print(time('g.Greedy()', mySetup))
    g.Greedy()
    print(g.tourValue())
    print('**********************************************')

    mySetup = '\n'.join((
        'import graph',
        'g = graph.Graph(-1, "plantedSoln.txt")'
    ))
    print(time('g.nearestInsertion()', mySetup))
    g.nearestInsertion()
    print(g.tourValue())
    print('**********************************************')
