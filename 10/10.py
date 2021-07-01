from os.path import realpath
from math import inf
from collections import defaultdict


def dijkstra(graph: dict, weight: dict, source: str, dest: str) -> int:
    Q = list(graph.keys())
    A, d, p = [], {}, {}

    for v in Q:
        d[v] = inf
        p[v] = None

    d[source] = 0

    while Q:
        u = min(Q, key=lambda x: d[x])
        A.append(u)
        Q.remove(u)

        for v in set(graph[u]).intersection(Q):
            alt = d[u] + weight[u + v]
            if d[v] > alt:
                d[v] = alt
                p[v] = u

        if u == dest:
            break

    return d[dest]


def main():
    inp = open(f'{realpath(__file__)[:-2]}txt').read()

    graph = defaultdict(list)
    weight = {}

    for transaction in inp.split('\n')[1:]:
        s, d, c = transaction.split(',')
        graph[s].append(d)
        weight[s + d] = int(c)

    print(dijkstra(graph, weight, 'TUPAC', 'DIDDY'))


if __name__ == '__main__':
    main()