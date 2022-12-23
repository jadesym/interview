class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edges = {}
        for from_person, to_person in dislikes:
            if from_person not in edges: edges[from_person] = set()
            edges[from_person].add(to_person)
            if to_person not in edges: edges[to_person] = set()
            edges[to_person].add(from_person)

        node_colors = {}
        while len(edges) > 0:
            node = next(iter(edges))
            if not self.dfs(node, edges, node_colors): return False
        return True

    def dfs(self, root: int, edges: Dict[int, Set[int]], node_colors: Dict[int, bool]) -> bool:
        # True is even
        # False is odd
        queue = [(root, True)]
        while len(queue) > 0:
            val, color = queue.pop()
            if val in node_colors and node_colors[val] != color: return False
            if val not in node_colors:
                node_colors[val] = color
                if val not in edges: continue
                new_vals = edges[val]
                del edges[val]
                for new_val in new_vals:
                    queue.append((new_val, not color))
        return True


