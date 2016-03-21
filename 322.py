class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1


test = Solution()
print(test.coinChange([1], 0))
print(test.coinChange([186,419,83,408], 6249))
