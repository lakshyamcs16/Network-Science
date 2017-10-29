import igraph
from igraph import Graph, summary, mean


karate = Graph.Read_GML("karate.gml")
g = igraph.Graph.Read_Ncol('karate.txt')
summary(karate)

g1=g.as_undirected()

def initialize():
    #no of vertices
    print("No of vertices",karate.vcount())
    #no of edges
    print("No of edges",karate.ecount())
    
    print("Degree of vertices",karate.degree())
    print("Mean: " , mean(karate.degree()))
    
    igraph.plot(g1)

#community detection based on edge_betweenness
def comm_edge_betweenness():
    dendrogram = g1.community_edge_betweenness()
    clusters = dendrogram.as_clustering()
    igraph.plot(clusters)
    membership = clusters.membership
    print("Modularity based on edge_betweeness",g1.modularity(membership,weights=None))

def comm_greedy_opt():
    #community detection based on greedy optimization of modularity
    dendrogram2 = g1.community_fastgreedy()
    clusters2 = dendrogram2.as_clustering()
    igraph.plot(clusters2)
    membership2 = clusters2.membership
    print("Modularity based on greedy optimization",g1.modularity(membership2,weights=None))

def comm_label_prop():
    #community detection based on propagating labels
    dendrogram4=g1.community_label_propagation()
    #clusters4 = dendrogram4.as_clustering()
    igraph.plot(dendrogram4)
    membership4 = dendrogram4.membership
    print("Modularity based on propagating labels",g1.modularity(membership4,weights=None))


def comm_random_walks():
    #community detection based on random walks
    dendrogram3=g1.community_walktrap()
    clusters3 = dendrogram3.as_clustering()
    igraph.plot(clusters3)
    membership3 = clusters3.membership
    print("Modularity based on random walks",g1.modularity(membership3,weights=None))

initialize()
comm_edge_betweenness()
comm_greedy_opt()
comm_label_prop()
comm_random_walks()
