#!/usr/bin/python3
"""Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # For each coin value, update the dp array with the minimum number of coins needed
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the last element in dp is still float('inf'), it means the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

# Example usage:
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3
