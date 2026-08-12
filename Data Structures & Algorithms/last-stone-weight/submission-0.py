class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1 : return stones[0]
        
        inverted_weights_stones = [ -val for val in stones ]

        heapq.heapify(inverted_weights_stones)


        while len(inverted_weights_stones) > 1 :
            
            if inverted_weights_stones[0] == inverted_weights_stones[1] :
                heapq.heappop(inverted_weights_stones) 
                heapq.heappop(inverted_weights_stones) 
            elif inverted_weights_stones[0] < inverted_weights_stones[1] :
                y = heapq.heappop(inverted_weights_stones) 
                x = heapq.heappop(inverted_weights_stones) 
                heapq.heappush(inverted_weights_stones, y - x)
            else :
                y = heapq.heappop(inverted_weights_stones) 
                x = heapq.heappop(inverted_weights_stones) 
                heapq.heappush(inverted_weights_stones, x - y)

            print(inverted_weights_stones)

        return - inverted_weights_stones[0] if inverted_weights_stones != [] else 0