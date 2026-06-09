import dsc40graph

def slc(graph, d, k):
    '''
    Performs single linkage clustering using Kruskal's algorithm.
    '''
    clusters = [{node} for node in graph.nodes]

    edges = list(graph.edges)
    edges.sort(key=d)

    for edge in edges:
        if len(clusters) == k:
            break

        u, v = edge

        u_cluster = None
        v_cluster = None

        for cluster in clusters:
            if u in cluster:
                u_cluster = cluster
            if v in cluster:
                v_cluster = cluster

        if u_cluster != v_cluster:
            new_cluster = u_cluster | v_cluster

            clusters.remove(u_cluster)
            clusters.remove(v_cluster)
            clusters.append(new_cluster)

    return frozenset(frozenset(cluster) for cluster in clusters)
