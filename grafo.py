## Importamos las bibliotecas
### PAra obter el grafo
from typing import FrozenSet
import osmnx as ox
## Para obtener la información de los nodos
import matplotlib.pyplot as plt
## Para manejar el grafo
import networkx as nx


## Obtenemos el grafo segun un lugar
def getGrafo(place_name):
    ## lugar donde buscaremos
    # place_name = 'Arequipa, Peru'

    graph = ox.graph_from_place(place_name)
    # graph = ox.graph_from_place(place_name, network_type='drive')
    return graph

## Obtenemos el grafo segun un lugar
def getGrafo(nort, south, east, west):
    graph = ox.graph_from_bbox(nort, south, east, west)
    # graph = ox.graph_from_place(place_name, network_type='drive')
    return graph



## graph es un objeto de Multigraph
## https://networkx.org/documentation/stable/reference/classes/multigraph.html#

# Podemos imprimir el grafo con networkx
def dibujarNetworkx(graph, with_labels=False):
    nx.draw(graph, with_labels=with_labels)

## Referencia basica para networkx
#https://networkx.org/documentation/stable/reference/introduction.html#graphs

## Dibuja el grafo
def dibujarOsm(graph):
    fig, ax = ox.plot_graph(graph)
    
## Dobuja el recorrido con OSm
def dibujarOsmRecorrido(graph, recorrido):
    fig, ax = ox.plot_graph_route(graph, recorrido)

def getNodos(graph):
    return graph.nodes

def getAristas(graph):
    return graph.edges

def algoritmoDijkstra(graph, origen, destino):
    return nx.dijkstra_path(graph, origen, destino)


## Casos de prueba

## Cuatro puntos - Mariano Melgar
nort = -16.3948
south = -16.4139
east = -71.4917
west = -71.5169

# place_name = 'Arequipa, Peru'
place_name = 'Arequipa, Peru'

graph = getGrafo(nort, south, east, west)

dibujarOsm(graph)

nodos = list(getNodos(graph))
aristas = list(getAristas(graph))

incio = nodos[1]
final = nodos[-1]

recorrido = algoritmoDijkstra(graph, incio, final)
print("Recorrido:" , recorrido)

dibujarOsmRecorrido(graph, recorrido)


## ---------------
## Adicional

## USAR NETWORKX
#https://www.youtube.com/watch?v=3OLw5-Iw7as

## OSMNX
#https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=to_gdfs#module-osmnx.plot
    ## Plot - dibuja
    ## graph - grafos
    
## ORIGINAL
#https://revistas.ulima.edu.pe/index.php/CIIS/article/view/5583/5270

## NetworkX
#https://networkx.org/documentation/stable/reference/introduction.html
#https://networkx.org/documentation/stable/tutorial.html#edges


