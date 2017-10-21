'''
Created on Oct 20, 2017

@author: Lakshya
'''
import igraph
from igraph import summary

g = igraph.read("socfb-Amherst41.mtx" , format="edge")
dg = igraph.read("web-EPA.edges", format="edge")

def undirected():
    summary(g)

    print("Eigenvector centrality of an undirected graph")
    l = g.eigenvector_centrality(directed=False, return_eigenvalue=True)  
    printVector(l)
    print("Eigen value is "+str(l[1]))

def directed():
    summary(dg)

    print("Eigenvector centrality of an directed graph")
    l = dg.eigenvector_centrality(directed=True, return_eigenvalue=True)  
    printVector(l)
    print("Eigen value is "+str(l[1]))

def printVector(l):
    x = 1
    for  i in l[0]:
        print(str(round(i,5))+"\t\t"),
        if x%4 == 0:
            print "\n"
        x+=1
  
undirected()
directed()