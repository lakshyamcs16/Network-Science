'''
Created on Oct 20, 2017
#http://networkrepository.com brilliant website for network repo!
@author: Lakshya
'''
import igraph
from igraph import summary, mean
from math import log
import matplotlib.pyplot as plt
from itertools import groupby

g = igraph.read("socfb-Amherst41.mtx" , format="edge")
summary(g)

def degree_frequency():
    l = list(g.degree_distribution().bins())
    
    deg = []
    for i in l:
        deg.append(str(i).replace(')',',').split(',')[2])

    deg = map(int, deg)
    deg.sort()
    deg_freq = [len(list(group)) for key, group in groupby(deg)]
    deg_freq.sort(reverse=True)
    
    return deg_freq

def powerlaw():
   
    plt.plot(degree_frequency())
    plt.title("Degree distribution graph")
    plt.ylabel("number of nodes with k links")
    plt.xlabel("number of links [k]")
    plt.show()
    
def smallworld():
    print("Small World Property")
    print(log(g.vcount()) / log(mean(g.degree())))
    
def clusteringCoeff():
    print("Global clustering coefficient")
    print(g.transitivity_undirected())
    
def showRealNetwork():
    powerlaw()
    smallworld()
    clusteringCoeff()

showRealNetwork()