class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp_array = [10 ** 4 + 1] * (amount + 1)
        dp_array[0] = 0

        coins.sort()

        for n in range(1, amount + 1) :
            for coin in coins :
                if coin > n : break
                dp_array[n] = min(dp_array[n], dp_array[n - coin] + 1)

        print(dp_array)

        result = dp_array[amount] 
        if result >= 10 ** 4 + 1 : return -1
        return result