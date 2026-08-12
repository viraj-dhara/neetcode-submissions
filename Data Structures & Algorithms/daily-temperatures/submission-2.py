class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0 for _ in range(len(temperatures))]

        for i, value1 in enumerate(temperatures) :
            for j, value2 in enumerate(temperatures[i+1:]) :
                if value2 > value1 :
                    output[i] = j+1
                    break


        return output

