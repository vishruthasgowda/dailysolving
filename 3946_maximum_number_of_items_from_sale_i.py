
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for factor, price in items:
            min_price = min(min_price, price)

            # Count purchased item + free items
            count = sum(
                f % factor == 0 for f, p in items
            )

            # 0/1 Knapsack
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        # Spend remaining budget on cheapest items
        ans = 0

        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // min_price)

        return ans
