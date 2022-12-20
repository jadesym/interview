import copy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        resultPaths = []
        self.dfs(graph, [0], resultPaths, len(graph))
        return resultPaths
    def dfs(self, graph: List[List[int]], pathSoFar: List[int], resultPaths: List[List[int]], n: int) -> None:
        lastNode = pathSoFar[len(pathSoFar) - 1]
        if lastNode == n - 1:
            resultPaths.append(pathSoFar)
        nextNodes = graph[lastNode]
        for nextNode in nextNodes:
            newPath = copy.deepcopy(pathSoFar)
            newPath.append(nextNode)
            self.dfs(graph, newPath, resultPaths, n)

        
        