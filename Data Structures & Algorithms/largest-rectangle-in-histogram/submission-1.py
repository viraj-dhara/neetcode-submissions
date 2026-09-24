class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        pre_smallest = [-1] * len(heights)
        post_smallest = [len(heights)] * len(heights)
        stack = list()
        max_area = 0

        for i in range(len(heights)) :

            if not stack : 
                stack.append(i)
                continue

            if heights[stack[-1]] < heights[i] :
                pre_smallest[i] = stack[-1]
                stack.append(i)
                continue
            
            while stack and heights[stack[-1]] >= heights[i] :
                stack.pop()
            
            pre_smallest[i] = stack[-1] if stack else pre_smallest[i]
            stack.append(i)


        stack = list()
            
        for i in range(len(heights) - 1, -1, -1) :

            if not stack : 
                stack.append(i)
                continue

            if heights[stack[-1]] < heights[i] :
                post_smallest[i] = stack[-1]
                stack.append(i)
                continue
            
            while stack and heights[stack[-1]] >= heights[i] :
                stack.pop()
            
            post_smallest[i] = stack[-1] if stack else post_smallest[i]
            stack.append(i)
        

        
        for i, height in enumerate(heights) :
            max_area = max(max_area, height * (post_smallest[i] - pre_smallest[i] - 1))
                
        return max_area
        