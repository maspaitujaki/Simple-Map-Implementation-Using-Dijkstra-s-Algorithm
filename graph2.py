from turtle import distance
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

class Graph:
    def __init__(self,pathName):
        self.graph = matAdjToDictGraph(pathName)

def readMatrixAdjTxt(pathName):
    with open(pathName) as f:
        n = [int(x) for x in next(f).split()]
        array = [[int(x) for x in line.split()] for line in f]
    return array

def matAdjToDictGraph(pathName):
    mat = readMatrixAdjTxt(pathName)
    n = len(mat)
    G = {}
    for i in range(n):
        v = {}
        for j in range(n):
            if(mat[i][j] != 0 and i != j ):
                v[j] = mat[i][j]
        G[i] = v
    return G

def drawDictGraph(graph):
    nxG = nx.DiGraph()
    # print(graph.graph)
    G = graph.graph
    V = [str(i) for i in range(len(G))]
    E = []
    for key, value in G.items():
        for key2, value2 in value.items():
            E.append((str(key),str(key2), value2))
    nxG.add_nodes_from(V)
    nxG.add_weighted_edges_from(E)
    weight = nx.get_edge_attributes(nxG,'weight')
    pos = nx.spring_layout(nxG)
    nx.draw(nxG,pos=pos, with_labels=True)
    nx.draw_networkx_edge_labels(nxG,pos,edge_labels=weight)
    plt.show()

def shortestDistanceNode(distances, visited):
    # create a default value for shortest
	shortest = None
	
  	# for each node in the distances object
	for key, value in distances.items():
    	# if no node has been assigned to shortest yet
  		# or if the current node's distance is smaller than the current shortest
		currentIsShortest =	shortest is None or distances[key] < distances[shortest]
        	
	  	# and if the current node is in the unvisited set
		if currentIsShortest and not key in visited:
            # update shortest to be the current node
			shortest = key
	return shortest

G1 = Graph("tc1.txt")
print(G1.graph)
# drawDictGraph(G1)
print(G1.graph[0])
print(shortestDistanceNode(G1.graph[0], {}))

