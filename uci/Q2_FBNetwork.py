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
    
    log_deg = []
    for i in deg_freq:
        x = log(i)
        log_deg.append(x)
        
    return {'log':log_deg, 'deg':deg_freq}


def powerlaw():
   
    log_log = degree_frequency()["log"]
    deg = degree_frequency()["deg"]
    print(log_log)
    plt.plot(log_log)
    plt.title("Degree distribution graph on log-log scale")
    plt.ylabel("log of number of nodes")
    plt.xlabel("log of Degree [k]")
    plt.show()
    
    plt.plot(deg)
    plt.title("Degree distribution graph")
    plt.ylabel("number of nodes")
    plt.xlabel("Degree [k]")
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
