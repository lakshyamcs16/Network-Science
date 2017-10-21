'''
Created on Sep 7, 2017

@author: Lakshya
'''
from igraph import Graph
from igraph import summary
from igraph import plot, mean

import plotly.plotly as py
import plotly.graph_objs as go
import plotly

karate = Graph.Read_GML("karate.gml")

summary(karate)
print("Degree of vertices",karate.degree())
print("Mean: " , mean(karate.degree()))
print("Betweeness: ", karate.edge_betweenness())

plotly.tools.set_credentials_file(username='apooos3', api_key='z2yZqlKj1z4JA6WR938R')
sorted_list = sorted(karate.degree())

data = [
    go.Box(
        y=sorted_list,
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8
    )
]
py.iplot(data)




plot(karate)
