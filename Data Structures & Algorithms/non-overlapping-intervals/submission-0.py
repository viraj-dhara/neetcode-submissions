class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        initial = len(intervals)
        intervals.sort(key = lambda item : item[0])

        print(f"{intervals = }")

        new_intervals = [intervals.pop(0)]
        prev_end = new_intervals[0][1]
        print(prev_end)

        for start, end in intervals :
            if start < prev_end :
                new_intervals[-1][1] = min(end, prev_end)
            else :
                new_intervals.append([start, end])

            prev_end = new_intervals[-1][1]

        print(new_intervals)

        return initial - len(new_intervals)
        