import math
import random

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        numOfLines = 0
        if n == -1:
            with open(filename, "r") as contents:
                for line in contents:
                    numOfLines += 1
            self.n = numOfLines
            self.dists = [[0 for i in range(self.n)]for j in range(self.n)]

            with open(filename, "r") as contents:
                data = [list(map(int, line.split())) for line in contents]
                for i in range(self.n):
                    for j in range(self.n):
                        self.dists[i][j] = euclid(data[i], data[j])
        else:
            self.n = n
            self.dists = [[0 for i in range(self.n)]for j in range(self.n)]
            with open(filename, "r") as contents:
                for line in contents:
                    lineContents= line.split()
                    map_listContents = map(int, lineContents)
                    int_lineContents = list(map_listContents)
                    self.dists[int_lineContents[0]][int_lineContents[1]] = int_lineContents[2]
                    self.dists[int_lineContents[1]][int_lineContents[0]] = int_lineContents[2]
        self.perm = list(range(self.n))
    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        totalCost = 0.0
        lastNode = self.n -1
        for i in range(self.n):
            if i == lastNode:
                totalCost = totalCost + self.dists[self.perm[i]][self.perm[(i+1)%self.n]]
            else:
                totalCost = totalCost + self.dists[self.perm[i]][self.perm[(i+1)%self.n]]
        return totalCost




    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.


    def trySwap(self,i):
        beforeCurrentCost =  self.dists[self.perm[(i-1)%self.n]][self.perm[i]]
        currentCost = beforeCurrentCost + self.dists[self.perm[i]][self.perm[(i+1)%self.n]] + self.dists[self.perm[(i+1)%self.n]][self.perm[(i+2)%self.n]]
        beforeSwappedCost = self.dists[self.perm[(i-1)%self.n]][self.perm[(i+1)%self.n]]
        swappedCost = beforeSwappedCost + self.dists[self.perm[(i+1)%self.n]][self.perm[i]] + self.dists[self.perm[i]][self.perm[(i+2)%self.n]]
        if swappedCost < currentCost:
            beingSwapped = self.perm[i]
            self.perm[i] = self.perm[(i+1)%self.n]
            self.perm[(i+1)%self.n] = beingSwapped
            return True
        else:
            return False





    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.

    def tourValueArray(self, reversedList):
        totalCost = 0.0
        for i in range(self.n):
            totalCost = totalCost + self.dists[reversedList[i]][reversedList[(i+1)%self.n]]
        return totalCost



    def tryReverse(self,i,j):
        #print('{} {}'.format(i, j))
        currentItoJ = self.tourValue()
        reversedList = self.perm[0:i] + (self.perm[i:(j+1)][::-1]) + self.perm[(j+1):]
        newItoJ = self.tourValueArray(reversedList)
        if newItoJ < currentItoJ:
            self.perm = list(reversedList)
            return True
        else:
            return False
        return False







    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True


    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True



    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def checkNextNodes(self,currNode, currIndex, visitedNodes):
        notChosenNodes = [n for n in range(self.n) if n not in visitedNodes]
        currentLowest = notChosenNodes[0]
        for j in (notChosenNodes):
            newCost = self.dists[currNode][j]
            oldCost = self.dists[currNode][currentLowest]
            if newCost < oldCost and j not in visitedNodes:
                currentLowest = j
        return currentLowest


    def Greedy(self):
        visitedNodes = []
        for i in range(0,(self.n -1)):
            visitedNodes.append(self.perm[i])
            #print(visitedNodes)
            self.perm[(i+1)] = self.checkNextNodes(self.perm[i], (i), visitedNodes)



#Part C- Your Own Algorithm
    def findShortestDistance(self,subtour,visitedNodes):
        notChosenNodes = [n for n in range(self.n) if n not in visitedNodes]
        #subtour[-1] is the tail element in the subtour
        #so sets intially currentLowestIndcies i.e distance from one node to another
        #as the first unviisted node and the last node of the subtour
        currentLowest = notChosenNodes[0]
        currentLowestIndices = (subtour[-1],currentLowest)
        for i in subtour:
            for j in notChosenNodes:
                newShortest = self.dists[i][j]
                oldShortest = self.dists[i][currentLowest]
                if newShortest < oldShortest and j not in visitedNodes and i != j:
                    currentLowest = j
                    currentLowestIndices = (i,j)
        return currentLowestIndices

    def nearestInsertion(self):
        newTour = [0]
        visitedNodes = [0]
        for i in range(self.n -1):
            #self.perm[:(i+1)%self.n] is current subtour
            indexInserted = self.findShortestDistance(self.perm[:(i+1)%self.n], visitedNodes)
            newTour.insert((indexInserted[0] +1), indexInserted[1])
            visitedNodes.append(indexInserted[1])
        self.perm = newTour
