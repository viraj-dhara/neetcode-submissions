class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points_heap = list()
        for point in points :
            points_heap.append( (- math.sqrt(point[0] ** 2 + point[1] ** 2), point[0], point[1]) )
        
        heapq.heapify(points_heap)

        print(points_heap)

        while len(points_heap) > k :
            heapq.heappop(points_heap)

        points = [ [ item[1], item[2] ] for item in points_heap ]

        return points