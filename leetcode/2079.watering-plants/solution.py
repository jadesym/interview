class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            steps += 1
            plant = plants[i]
            if plant > cur_capacity:
                steps += i * 2
                cur_capacity = capacity - plant
            else:
                cur_capacity -= plant
            # print(i, plants[i], steps)

        return steps
            
            