class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps = 0
        idx = 0
        can_capacity = capacity

        while idx < len(plants):
            
            needed_water = plants[idx]

            if needed_water <= can_capacity:

                steps += 1
                can_capacity -= needed_water

            else:

                steps = steps + idx + (idx + 1)

                can_capacity = capacity
                can_capacity -= needed_water   

            idx += 1
                
        return steps
    