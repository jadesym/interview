class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_travel_distances = []
        total_so_far = 0
        for distance in travel:
            total_so_far += distance
            total_travel_distances.append(total_so_far)

        metal_total = 0
        last_metal_index = None
        paper_total = 0
        last_paper_index = None
        glass_total = 0
        last_glass_index = None

        for i in range(len(garbage)):
            for letter in garbage[i]:
                if letter == "G":
                    glass_total += 1
                    last_glass_index = i
                elif letter == "M":
                    metal_total += 1
                    last_metal_index = i
                elif letter == "P":
                    paper_total += 1
                    last_paper_index = i
        total_cost = 0
        if metal_total != 0:
            if last_metal_index > 0:
                total_cost += total_travel_distances[last_metal_index - 1]
            total_cost += metal_total 
        if paper_total != 0:
            if last_paper_index > 0:
                total_cost += total_travel_distances[last_paper_index - 1]
            total_cost += paper_total
        if glass_total != 0:
            if last_glass_index > 0:
                total_cost += total_travel_distances[last_glass_index - 1]
            total_cost += glass_total
        return total_cost