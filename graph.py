import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def readMatrixAdjTxt(pathName):
    with open(pathName) as f:
        n = [int(x) for x in next(f).split()]
        array = [[int(x) for x in line.split()] for line in f]
    
    matAdjToGraphNx(array)
    

def matAdjToGraphNx(mat):
    G = nx.DiGraph()
    V = [str(i) for i in range(len(mat))]
    E = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != 0:
                E.append((str(i),str(j),mat[i][j]))
    G.add_nodes_from(V)
    G.add_weighted_edges_from(E)
    weight = nx.get_edge_attributes(G,'weight')
    pos = nx.spring_layout(G)
    nx.draw(G,pos=pos, with_labels=True)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight)
    plt.show()
    # return G


readMatrixAdjTxt("tc1.txt")
# weight = nx.get_edge_attributes(G,'weight')
# nx.draw(G, with_labels=True)
# nx.draw_networkx_edge_labels(G,edge_labels=weight)

