# iterative
def DFS_traversal_iter(graph, start):
    vertex_list, edge_list = graph
    # initialise our adj list
    adjacency_list = [[] for vertex in vertex_list]
    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])
    # print(adjacency_list)
    # let’s use a stack
    stack = [start]
    visitedVertex = []

    while stack:
        current = stack.pop()
        for neighbor in adjacency_list[current]:
            if neighbor not in visitedVertex:
                stack.append(neighbor)

        if current not in stack:
            visitedVertex.append(current)

    return visitedVertex


# ------------

## TODO: recursive, dealing with left and right trees
# recursive
def DFS_traversal_rec(graph, start, visited=None):

    if visited is None:
        visited = set()
    visited.add(start)

    # print(start)
    # choose a neighbor of the current node (start) and explore it as long it is not visited
    for next in graph[start] - visited:
        DFS_traversal_rec(graph, next, visited)
    return visited


if __name__ == '__main__':

    vertex_list = ['0', '1', '2', '3', '4']
    edge_list = [
        (2, 4), (2, 1), (2, 0), (3, 0), (4, 2), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2)]
    graph = (vertex_list, edge_list)

    print("Following is Depth First Traversal: ")
    path = DFS_traversal_iter(graph, 0)
    print(path)

    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    path = DFS_traversal_rec(graph, '0')
    print(path)
