class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cumulative_costs = [0] * (len(cost) + 1)
        cost.append(0)

        for i in range(len(cumulative_costs)) :
            if i == 0 or i == 1: cumulative_costs[i] = cost[i]
            else :
                cumulative_costs[i] = min(cumulative_costs[i-1], cumulative_costs[i-2]) + cost[i]
        print(cumulative_costs)
        return cumulative_costs[len(cost)-1]