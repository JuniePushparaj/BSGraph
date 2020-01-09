from helper.Queue import Queue


class BFS:
    def __init__(self):
        self.queue = Queue()

    def getPath(self, edges, source, destination):
        self.queue.EnQueue(source)
        visitedNodes = [0] * len(edges)
        visitedNodes[source] = 1
        path = []
        pathExists = False
        while(not self.queue.isEmpty()):
            adjacentNodes = [index for index, value in enumerate(
                edges[self.queue.front.data]) if value == 1 and visitedNodes[index] == 0]
            pathNode = self.queue.DeQueue()
            if len(adjacentNodes) > 0:
                path.append(pathNode)
            if pathNode == destination:
                pathExists= True
                break
            for node in adjacentNodes:
                self.queue.EnQueue(node)
                visitedNodes[node] = 1
        if pathExists:
            return path
        else:
            return []
