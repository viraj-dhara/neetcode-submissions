class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        
        n = len(queries)

        query_to_index = defaultdict(list)
        for i, query in enumerate(queries) :
            query_to_index[query].append(i)
        queries.sort()

        
        intervals.sort()
        results = [-1] * n
        st_idx_intervals = 0
        valid_heap = list()


        for query in queries : 

            while st_idx_intervals < len(intervals) and query >= intervals[st_idx_intervals][0] :
                heapq.heappush(valid_heap, (intervals[st_idx_intervals][1] - intervals[st_idx_intervals][0] + 1, intervals[st_idx_intervals][1]))
                st_idx_intervals += 1

            while valid_heap and query > valid_heap[0][1] :
                heapq.heappop(valid_heap)

            if not valid_heap :
                continue
            else :
                for index in query_to_index[query] :
                    results[index] = valid_heap[0][0]


        return results