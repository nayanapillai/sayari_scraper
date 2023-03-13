import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the CSV file into a pandas DataFrame
data = pd.read_csv('companies.csv')

# create a new directed graph
G = nx.DiGraph()

# add the companies, registered agents, and owners as nodes
for index, row in data.iterrows():
    G.add_node(row['Company'])
    G.add_node(row['Registered Agent'])
    G.add_node(row['Owners'])

# add the edges between the companies, registered agents, and owners
for index, row in data.iterrows():
    G.add_edge(row['Registered Agent'], row['Company'])
    G.add_edge(row['Company'], row['Owners'])

# draw the graph using matplotlib
pos = nx.spring_layout
