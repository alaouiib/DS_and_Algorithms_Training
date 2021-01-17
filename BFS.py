
# iterative bfs traversal
def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [set() for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].add(edge[1])
    print('adjacencyList:', adjacencyList)
    # bfs
    while queue:
        current = queue.pop(0)  # dequeue
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)  # enqueue
        if current not in queue:
            visitedList.append(current)

    # what if a graph is having two different disconnected parts
    if len(vertexList) != len(visitedList):
        print('graph has two different disconnected parts')
        diff_part = list(set(vertexList) - set(visitedList))
        visitedList.extend(diff_part)
    return visitedList


if __name__ == '__main__':

    vertexList = [0, 1, 2, 3, 4, 5, 6, 7]
    edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (3, 1),
                (2, 0), (2, 4), (2, 5), (4, 6), (6, 4)]

    graphs = (vertexList, edgeList)

    print("Following is Breadth First Traversal: ")
    print(bfs(graphs, 0))
