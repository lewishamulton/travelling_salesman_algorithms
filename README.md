# travelling_salesman_algorithms

These files were part of my submission to the 3rd Introduction to Algorithms and Data Structures Coursework. This involves various implementations of the travelling salesman algorithm as well as creating my own algorithm, based on further research into various heurisitics used for this popular Algorithms problem. 

The file graph.py contains various implementations of the travelling salesman algorithm. It can take in Euclidean files which will contain just the points/nodes of the graph, each point described as a pair of integers (the x and y coordinates) on a single line, without any formatting. These are the cities25, cities50, cities75 files. The flag of -1 is used for this 
It can also take in non-Euclidean files where each line of the input file describes one edge of the graph, each line containing three integers, these being the first endpoint i, the second endpoint j and the given weight/distance for the edge between i and j. An input value of n, where n is the number of nodes in the input graph is used. sixnodes is an example of this type of file. 

To run the algorithms you could do
```
import graph 
g = graph.Graph(-1,"cities50")
g.swapHeuristic()
g.tourValue()
```

and it will return a total cost of the tour

There is also a file tests.py which has methods that return the times taken for the algorithms to return solutions to a randomnly generated Euclidean Graph and a graph with an optimal but planted solution.   

