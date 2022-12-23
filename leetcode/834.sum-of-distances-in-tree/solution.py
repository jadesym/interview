class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        edge_map = {}
        for from_node, to_node in edges:
            if from_node not in edge_map: edge_map[from_node] = set()
            edge_map[from_node].add(to_node)
            if to_node not in edge_map: edge_map[to_node] = set()
            edge_map[to_node].add(from_node)

        visited_set = set()
        zero_root_map = {}
        queue = [0]
        while len(queue) > 0:
            node = queue.pop()
            if node not in zero_root_map:
                zero_root_map[node] = set()

            for to_node in edge_map[node]:
                if to_node in visited_set: continue
                zero_root_map[node].add(to_node)
                queue.append(to_node)

            visited_set.add(node)

        # print(zero_root_map)
        node_counts = {}

        root_count, root_distance = self.dfs(0, zero_root_map, node_counts)

        new_visited_set = set()
        result = [0] * n
        queue = [(0, root_distance)]
        while len(queue) > 0:
            node, distance = queue.pop()
            result[node] = distance
            new_visited_set.add(node)
            if to_node not in zero_root_map: continue
            for to_node in zero_root_map[node]:
                if to_node in new_visited_set: continue
                cur_node_count = node_counts[to_node]
                to_node_distance = distance - cur_node_count + n - cur_node_count
                queue.append((to_node, to_node_distance))
        return result

    # (node_count, subtree_root_distance)
    def dfs(self, node: int, zero_root_map: Dict[int, Set[int]], node_counts: Dict[int, int]) -> (int, int):
        if node not in zero_root_map:
            node_counts[node] = 1
            return (1, 0)
        to_nodes = zero_root_map[node]
        if len(to_nodes) == 0:
            node_counts[node] = 1
            return (1, 0)

        count = 1
        distances = 0
        for to_node in to_nodes:
            to_node_count, to_node_distance = self.dfs(to_node, zero_root_map, node_counts)

            count += to_node_count
            distances += to_node_count + to_node_distance
        node_counts[node] = count
        return (count, distances)
        
