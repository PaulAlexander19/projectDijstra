import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx


g = nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
print(g.number_of_nodes())
print(g.number_of_edges())
g.add_edge(1, 2)
print(g.number_of_edges())


# # nodes , edges = ox.graph_to_gdfs(graph)

# print(nodes)
# print(edges.head())



# area = ox.gdf_from_place(place_name)

# area2 = ox.plot.plot_figure(graph, fig=fig, ax=ax, figsize=(12,8))
# area.plot()


# print(graph.nodes.data())