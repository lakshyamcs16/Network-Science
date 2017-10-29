'''
Created on Oct 20, 2017

@author: Lakshya
'''
from igraph import summary, Graph

g = Graph.Read_Ncol("weighted_graph.edges", weights=True, directed=True)
dg = Graph.Read_Ncol("unweighted_graph.edges", weights=False, directed=True)
weighted_ev = ''
unweighted_ev = ''

def printeigenvalue(value):
    print("\n")
    print(value)
    
def weighted():
    summary(g)

    print("Eigenvector centrality of an undirected graph")
    l = g.eigenvector_centrality(directed=True, weights = g.es["weight"], return_eigenvalue=True)  
    printVector(l)
    return ("Eigen value of weighted graph is "+str(l[1]))

def unweighted():
    summary(dg)

    print("Eigenvector centrality of an directed graph")
    l = dg.eigenvector_centrality(directed=True, weights = None, return_eigenvalue=True)  
    printVector(l)
    return("Eigen value of the same unweighted graph is "+str(l[1]))

def printVector(l):
    x = 1
    for  i in l[0]:
        print(str(round(i,5))+"\t\t"),
        if x%4 == 0:
            print "\n"
        x+=1
  
weighted_ev = weighted()
unweighted_ev = unweighted()
printeigenvalue(weighted_ev)
printeigenvalue(unweighted_ev)
