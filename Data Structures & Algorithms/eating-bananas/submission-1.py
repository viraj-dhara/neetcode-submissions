class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 0
        end = max(piles)
        mid = (start + end) // 2

        while start < end :
            mid = (start + end) // 2

            time_taken = 0
            for pile in piles :
                time_taken += math.ceil(pile/mid)

            if time_taken <= h :
                end = mid
            elif time_taken > h :
                start = mid + 1

            if end == 1 : return 1

        return start