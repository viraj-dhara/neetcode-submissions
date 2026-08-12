class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = list()
        counts = [0] * 2001

        for num in nums:
            counts[num+1000] += 1

        
        for _ in range(k):
            (index, max) = (0,0)
            for i, count in enumerate(counts):
                if count > max : 
                    index = i
                    max = count

            output.append(index-1000)
            counts[index] = 0

            

        return output