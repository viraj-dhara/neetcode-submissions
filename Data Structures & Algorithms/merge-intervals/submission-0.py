class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda interval : interval[0])
        intervals = deque(intervals)

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        next_start, next_end = 0, 0

        intervals.popleft()

        result = list()

        while intervals :

            next_start, next_end = intervals.popleft()

            if curr_end < next_start :
                result.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end

            else :
                curr_end = max(curr_end, next_end)

        result.append([curr_start, curr_end])

        return result



