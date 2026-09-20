class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append((position[i], (target-position[i])/speed[i]))
        stack.sort(reverse = True)
        count = 1
        curr_fleet_time = stack[0][1]
        for j in range(1,len(stack)):
            if curr_fleet_time < stack[j][1]:
                count += 1
                curr_fleet_time = stack[j][1]
        return count