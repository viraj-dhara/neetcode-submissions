class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals : return [newInterval]
        
        new_intervals = list()
        new_start, new_end = newInterval
        newIntervalInserted = False
        skipIteration = 0

        # print(f"{new_start, new_end = }\n")

        for index, interval in enumerate(intervals) :

            # print(f"{interval}    {new_intervals =}")

            if skipIteration :
                skipIteration -= 1
                continue
            if new_start > interval[1] or newIntervalInserted :
                new_intervals.append(interval)
            elif new_end < interval[0] :
                new_intervals.extend([newInterval, interval])
                newIntervalInserted = True
            elif new_start > interval[0] and new_end < interval[1] :
                new_intervals.append(interval)
                newIntervalInserted = True
            else :
                curr_start = min(new_start, interval[0])
                curr_end = max(new_end, interval[1])

                # print(f"{curr_start, curr_end = }")

                while index + 1 < len(intervals) and curr_end >= intervals[index + 1][0] :
                    curr_end = max(curr_end, intervals[index + 1][1])
                    index += 1
                    skipIteration += 1

                new_intervals.append([curr_start, curr_end])
                newIntervalInserted = True
                continue

        if not newIntervalInserted : new_intervals.append(newInterval)

        return new_intervals

