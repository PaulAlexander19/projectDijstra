from typing import Mapping
import networkx as nx
import osmnx as ox
from shapely.geometry import LineString, mapping
import geopandas as gpd
from ipyleaflet import *

place_name = "Kamppi, Helsinki, Finland"
graph = ox.graph_from_place(place_name)
fig, ax = ox.plot_graph(graph)

nodes, edges = ox.graph_to_gdfs(graph)
print(nodes)

center = (60.16607, 24.93116)
m = Map(center=center, basemap=basemaps.CartoDB.Positron, zoom=15)
#style for the destination marker
