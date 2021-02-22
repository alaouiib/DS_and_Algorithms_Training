
# TODO: Priority Queue implementation (Example of imp: https://leetcode.com/problems/network-delay-time/discuss/329376/efficient-oe-log-v-python-dijkstra-min-heap-with-explanation)
# ℹ Note that Dijkstra does not consider negatively weighted algorithms -> does not get you the shortest path always if there exist negative paths

import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)

INFINITY = float('inf')


def dijkstra(graph, start, end):
    vertex_list, edge_list = graph
    # setup graph (to be refined !)
    adjacency_list = {node: set() for node in vertex_list}
    for edge in edge_list:

        adjacency_list[edge[0]].add((edge[1], edge[2]))
    # print('adjacency list:')
    # pp.pprint(adjacency_list)

    # shortest path logic (returns path and distance)
    # step 1
    unvisited_nodes = [node for node in vertex_list]
    # print('unvisited_nodes',unvisited_nodes)
    # step 2
    distance_from_start = {
        node: (0 if node == start else INFINITY) for node in vertex_list
    }
    # this is to keep track of previous nodes from where we came
    # we update the array when we "relax" a node

    previous_node = {node: None for node in vertex_list}

    # print('distance_from_start')
    # pp.pprint(distance_from_start)
    # print('#'*60)
    # step 3
    while unvisited_nodes:
        # from the unvisited_nodes
        current_node = min(
            unvisited_nodes, key=lambda node: distance_from_start[node])
        unvisited_nodes.remove(current_node)
        # If current_node's distance is INFINITY, the remaining unvisited
        # nodes are not connected to start_node, so we're done.
        if distance_from_start[current_node] == INFINITY:
            break
        for neighbor, distance in adjacency_list[current_node]:
            cost_neighbor = distance_from_start[current_node] + distance
            if(cost_neighbor < distance_from_start[neighbor]):
                distance_from_start[neighbor] = cost_neighbor
                previous_node[neighbor] = current_node

            # stop condition
        if current_node == end:
            break  # we are done

    # pp.pprint(distance_from_start)
    # print(previous_node)

    path = []
# path construction (First Idea)
    for node, distance in previous_node.items():
        if distance and distance not in path:
            path.append(distance)
    path.append(end)
    # print(path)
    cost = distance_from_start[end]

# path construction (Second Idea using a que)
    # To build the path to be returned, we iterate through the nodes from
    # end_node back to start_node. Note the use of a deque, which can
    # appendleft with O(1) performance.

    # from collections import deque
    # path = deque()
    # current_node = end_node
    # while previous_node[current_node] is not None:
    #     path.appendleft(current_node)
    #     current_node = previous_node[current_node]
    # path.appendleft(start_node)

    return ('->'.join(path), cost)


if __name__ == '__main__':
    vertex_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edge_list = [('A', 'B', 5), ('A', 'C', 3), ('A', 'D', 6), ('C', 'E', 6), ('C', 'D', 7), ('B', 'C', 6), ('B', 'E', 4), ('E', 'F', 4), ('E', 'G', 3),
                 ('D', 'E', 2), ('D', 'F', 2), ('F', 'G', 5)]
    graph = (vertex_list, edge_list)

    path, cost = dijkstra(graph, 'A', 'F')
    print('Optimal Path:', path, '\nCost:', cost)
