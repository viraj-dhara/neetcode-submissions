class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        tasks_heap = list()
        tasks_freq = defaultdict(int)

        for task in tasks :
            tasks_freq[task] += 1

        for key in tasks_freq.keys() :
            heapq.heappush(tasks_heap, (-tasks_freq[key], key))

        cycle_count = 0
        my_queue = deque()

        while len(tasks_heap) != 0 or len(my_queue) != 0:
            
            cycle_count += 1
            
            if my_queue and cycle_count - my_queue[0][1] > n:
                task = my_queue.popleft()
                heapq.heappush(tasks_heap, task[0])

            if len(tasks_heap) == 0 : continue

            task = heapq.heappop(tasks_heap)
            
            if task[0] != -1 :
                task = (task[0] + 1, task[1])
                my_queue.append((task, cycle_count))
            

        return cycle_count