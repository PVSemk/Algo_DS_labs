import time
from collections import defaultdict
import heapq


def create_spanning_tree(graph, start):
    mst = defaultdict(set)
    visited = set()
    visited.add(start)
    edges = [
        (cost, start, destination)
        for destination, cost in graph[start].items()
    ]
    heapq.heapify(edges)
    while edges:
        cost, source, destination = heapq.heappop(edges)
        if destination not in visited:
            visited.add(destination)
            mst[source].add(destination)
            for destination_next, cost in graph[destination].items():
                if destination_next not in visited:
                    heapq.heappush(edges, (cost, destination, destination_next))

    return mst


def main():
    with open('sample2.txt', 'r') as file:
        adj_list = file.read().rstrip().split()

    vertex_amount = adj_list[0]
    edges_amount = adj_list[1]
    graph = {vertex: {} for vertex in range(1, int(vertex_amount) + 1)}
    # print(graph)
    for i in range(2, int(edges_amount)*3 + 2, 3):
        graph[int(adj_list[i])][int(adj_list[i+1])] = int(adj_list[i+2])
    # print(graph)
    span_tree = create_spanning_tree(graph, 1)

    count = 0
    for key in span_tree.keys():
        print(key, end=' ')
        count += 1
    print('\n', count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('\nTotal taken time: {:.5f}'.format(time.time() - start_time))
