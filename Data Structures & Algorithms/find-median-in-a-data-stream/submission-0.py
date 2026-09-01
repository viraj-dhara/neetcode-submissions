class MedianFinder:

    def __init__(self):
        
        self.upper_min_heap = list()
        self.lower_max_heap = list()

    def addNum(self, num: int) -> None:
        
        
        if self.lower_max_heap and num <=  -self.lower_max_heap[0] : heapq.heappush(self.lower_max_heap, - num)
        else : heapq.heappush(self.upper_min_heap, num)

        while len(self.lower_max_heap) - len(self.upper_min_heap) > 1 :
            heapq.heappush(self.upper_min_heap, -heapq.heappop(self.lower_max_heap))
        while len(self.upper_min_heap) - len(self.lower_max_heap) > 1 :
            heapq.heappush(self.lower_max_heap, -heapq.heappop(self.upper_min_heap))


    def findMedian(self) -> float:
        
        if (len(self.upper_min_heap) + len(self.lower_max_heap)) % 2 == 0 :
            return (self.upper_min_heap[0] - self.lower_max_heap[0]) / 2
        else :
            if len(self.upper_min_heap) > len(self.lower_max_heap) :
                return self.upper_min_heap[0]
            else :
                return -self.lower_max_heap[0]

