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

def findShortestPath(graph, startNode, endNode):
    # Menyimpan jarak Node dari startNode, dimulai dari endNode dengan jarak Infinity
    # dan node yang bertetangga dengan startNode
    distances = {}
    distances[endNode] = float('inf')
    for key, value in graph.graph[startNode].items():
        distances[key] = value

    # track parent dari node untuk menemukan path di akhir
    parents = { endNode : None }
    for key, value in graph.graph[startNode].items():
        parents[key] = startNode
    
    # simpan node yang telah divisit
    visited = []

    # menemukan node terdekat
    node = shortestDistanceNode(distances,visited)

    # Untuk node tersebut
    while(node):
        distance = distances[node]
        children = graph.graph[node]

        # tiap anak node
        for key,value in children.items():
            # Pastikan bukan start node
            if key == startNode: continue
            else:
                # Jarak dari start node ke child node
                newDistance = distance + value
                # Simpan newDistance ke dalam distances apabila
                # child tidak ada di distances atau newDistance
                # lebih pendek dari yang udh disimpan
                if (not key in distances.keys()) or distances[key] > newDistance:
                    distances[key] = newDistance
                    parents[key] = node
        
        # Tambahkan node ke dalam visited
        visited.append(node)
        # Pilih node dengan distances minimum
        node = shortestDistanceNode(distances, visited)
    

    shortestPath = [endNode]
    parent = parents[endNode]
    print(parents)
    while (parent):
        shortestPath.append(parent)
        parent = parents[parent]
    shortestPath.append(startNode)
    shortestPath.reverse()

    result = {
        "distance": distances[endNode],
        "path": shortestPath
    }

    return result
    
    

        
G1 = Graph("tc1.txt")
# print(G1.graph)
# drawDictGraph(G1)
# print(G1.graph[0])
# print(shortestDistanceNode(G1.graph[0], {}))
res = findShortestPath(G1, 0, 8)
print(res)
