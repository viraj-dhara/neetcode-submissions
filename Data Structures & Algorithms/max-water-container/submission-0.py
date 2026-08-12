class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        first = 0
        last = len(height) - 1

        max_vol = 0

        while(first<last) :
            _ = (last - first) * min(height[first], height[last])
            max_vol = max(max_vol, _ )

            if height[first] <= height[last] :
                first += 1
            else :
                last -= 1
        
        return max_vol