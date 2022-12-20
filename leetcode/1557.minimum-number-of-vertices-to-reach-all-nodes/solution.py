class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited_node_set = set()
        minimum_set = set()
        from_nodes = set()
        to_nodes = set()
        for fromNode, toNode in edges:
            from_nodes.add(fromNode)
            to_nodes.add(toNode)
        for from_node in from_nodes:
            if from_node not in to_nodes:
                minimum_set.add(from_node)
        return list(minimum_set)

