# http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search

# graph is in adjacent list representation
graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

# below implemented method is independednt, which is not inside any class.
def BreadthFirstSearch(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])

    while queue:

        path = queue.pop(0)

        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue        
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


print BreadthFirstSearch(graph, '1', '19')
