class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen_numbers = defaultdict(lambda: False)
        seen_numbers[n] = True

        while True : 

            n = sum([(int(item)) ** 2 for item in str(n)])

            if n == 1 : return True
            if seen_numbers[n] == True : return False

            seen_numbers[n] = True