class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        if sum(gas) < sum(cost) : return -1

        reserve_tank = 0

        curr_start = 0

        for station in range(len(gas)) :
            if cost[station] > gas[station] + reserve_tank :
                curr_start = station + 1
                reserve_tank = 0
            else :
                reserve_tank += gas[station] - cost[station]
                
        return curr_start if curr_start < len(gas) else -1