class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = height[:]
        suffix = height[:]

        for i in range(len(height)) :
            if i == 0 : continue
            prefix[i] = max(prefix[i], prefix[i - 1])
        
        for i in reversed(range(len(height))) :
            if i == len(height) - 1 : continue
            suffix[i] = max(suffix[i], suffix[i + 1])

        total_water = 0

        for i in range(len(height)) :
            if i == 0 or i == len(height) - 1 : continue

            total_water += max( 0, min( prefix[i], suffix[i] ) - height[i] )

        return total_water