import os
import random
import time
import sys
import math
import numpy as np
import networkx as nx


def enumerate_dag(g):
  def enumerate_r(n, paths, visited, a_path = []):
    a_path += [n]
    visited[n] = 1
    if not g[n]:
        paths += [list(a_path)]
    else:
        for nn in g[n]:
            enumerate_r(nn, paths, visited, list(a_path))

  paths, N = [], len(g)
  visited = np.zeros((N), dtype='int32')

  for root in range(N):
    if visited[root]: continue
    enumerate_r(root, paths, visited, [])

  return paths


def transitive_reduction(G):
    """
    References:
    https://en.wikipedia.org/wiki/Transitive_reduction
    """
    TR = nx.DiGraph()
    TR.add_nodes_from(G.nodes())
    for u in G:
        u_edges = set(G[u])
        for v in G[u]:
            u_edges -= {y for x, y in nx.dfs_edges(G, v)}
        TR.add_edges_from((u,v) for v in u_edges)
    return TR

#Get the longest path
def dag_longest_path(G, weight='weight', default_weight=1):
    if(G.number_of_edges() !=0):
        dist = {}
        for v in nx.topological_sort(G):
            us = [(dist[u][0] + data.get(weight, default_weight), u)
                for u, data in G.pred[v].items()]
            # Use the best predecessor if there is one and its distance is non-negative, otherwise terminate.
            maxu = max(us, key=lambda x: x[0]) if us else (0, v)
            dist[v] = maxu if maxu[0] >= 0 else (0, v)
        u = None
        v = max(dist, key=lambda x: dist[x][0])
        path = []
        while u != v:
            path.append(v)
            u = v
            v = dist[v][1]
        path.reverse()
        return path


def calculateAllChains(G):
    L = []
    c = []
    c = dag_longest_path(G)

    # Get nodes that have edges with other nodes
    while G.number_of_edges() != 0:
        G.remove_nodes_from(c)
        L.append(c)
        c = dag_longest_path(G)

    #Append the node that have no more edges
    for i in G.nodes():
        L.append([i])

    return L


def voraceApproximation(G):
    nbNode = G.number_of_nodes()

    longestChains = calculateAllChains(G)
    nbExtensionLineaire = len(longestChains)

    h = 0
    for i in range (1, nbExtensionLineaire):
        h += -(len(longestChains[i]) / G.number_of_nodes()) * (math.log(len(longestChains[i]) / G.number_of_nodes(), 2))

    expo = (0.5 * nbNode * h)
    nbExtensionLineaireApprox = math.pow(2, expo)


    return nbExtensionLineaireApprox


if __name__ == "__main__":
    G = nx.DiGraph();

    G.add_edges_from([(1, 0), (1, 4), (1, 8), (2, 5), (5, 8), (6, 0), (6, 2), (6, 4), (7, 2), (9, 3), (9, 6), (9, 7)])

    print(G.number_of_nodes(), G.number_of_edges())

    t = transitive_reduction(G)

    print(voraceApproximation(G))