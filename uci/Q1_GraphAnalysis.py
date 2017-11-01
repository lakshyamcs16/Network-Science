'''
Created on Oct 17, 2017

@author: Lakshya
'''
import pandas as pd
import numpy as np
from math import sqrt
from pandas import DataFrame
from igraph import Graph, plot
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

distances = np.zeros(shape=(150,150))
reduced_dist = []
quartile = 0
df = pd.read_csv("iris.csv")
sepal_length = np.array(df['Sepal length'])
sepal_width = np.array(df['Sepal Width'])
petal_length = np.array(df['Petal length'])
petal_width = np.array(df['Petal width'])

def distance():
    
    for i in range( 149 ):
        for k in range( i+1, 150 ):
            dist = sqrt(pow(sepal_length[i] - sepal_length[k], 2) + pow(sepal_width[i] - sepal_width[k], 2) + \
                                pow(petal_length[i] - petal_length[k], 2) + pow(petal_width[i] - petal_width[k], 2))
            distances[i][k] =  dist
    
    print('Euclidean distance matrix')        
    print DataFrame(distances.tolist())
    
    return distances

def findquartile():
    euc_dist = distance()
    temp_dist = euc_dist.flatten()
    j=0
    for i in temp_dist:
            if(i!=0):
                reduced_dist.insert(j, i)
                j +=1
            
            
    quartile = np.percentile(reduced_dist,25)
    print('First Quartile of the iris data set is')
    print(quartile)
    return quartile
    
def cuttOffEdge(edge_weight, threshold):
    
    if(edge_weight >= threshold):
        return True

def createGraph():
    threshold = findquartile()
    
    g = Graph()
    g.add_vertices(150)
    for src, i in enumerate(distances.tolist()):
        for dest, j in enumerate(i):
            if(cuttOffEdge(j, threshold)):
                g.add_edge(src, dest)
    
    #print g
    print('Radius of the generated graph is ')
    print(g.radius(mode="ALL"))
    print('Diameter of the generated graph is')
    print(g.diameter(directed=False, unconn=False, weights=None))
    print("Number of vertices:" + str(g.vcount()))
    print("Number of edges:" + str(g.ecount())) 
    plot(g.degree_distribution(2))

def createBoxPlot():
    plotly.tools.set_credentials_file(username='apooos3', api_key='********************')

    x = []
    for _ in range(50):
        x.append('setosa')
    for _ in range(50,100):
        x.append('versicolor')
    for _ in range(100,150):
        x.append('virginica')    
    
    
    trace0 = go.Box(
        y=sepal_length,
        x=x,
        name='Sepal length',
        marker=dict(
            color='#3D9970'
        )
    )
    trace1 = go.Box(
        y=sepal_width,
        x=x,
        name='Sepal width',
        marker=dict(
            color='#FF4136'
        )
    )
    trace2 = go.Box(
        y=petal_length,
        x=x,
        name='Petal length',
        marker=dict(
            color='#FF851B'
        )
    )
    trace3 = go.Box(
        y=petal_width,
        x=x,
        name='Petal width',
        marker=dict(
            color='#3BA0D2'
        )
    )
    data = [trace0, trace1, trace2, trace3]
    layout = go.Layout(
        yaxis=dict(
            title='Class wise boxplot',
            zeroline=False
        ),
        boxmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)
    print('Box plot successfully created. Go check plot.ly!')
    
    
createGraph()
createBoxPlot()
    
