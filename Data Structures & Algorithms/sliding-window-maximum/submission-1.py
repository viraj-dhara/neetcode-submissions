class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == k  :
            return [max(nums)]
        elif k == 1 :
            return nums
        
        lazy_max = list()
        result = list()

        for i in range(len(nums)) :
            
            heapq.heappush(lazy_max, ( - nums[i], i))

            while i - lazy_max[0][1] > k - 1 :
                heapq.heappop(lazy_max)

            if i + 1 >= k :
                result.append( - lazy_max[0][0])

        return result