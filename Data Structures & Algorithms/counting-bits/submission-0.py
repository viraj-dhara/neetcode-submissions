class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0 : return [0]
        if n == 1 : return [0, 1]

        dp_arrays = defaultdict(list)
        power = 1

        dp_arrays[0] = [0, 1]

        while 2 ** (power - 1) <= n :
            for i, item in enumerate(dp_arrays[power - 1]) :
                dp_arrays[power].append(item)
                dp_arrays[power].append(item + 1)

            power += 1

        return dp_arrays[power - 1][:n + 1]

        