# https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
class Solution:
    def minDifference(self, arr, n):
        totalSum = sum(arr)
        dp = [[False] * (totalSum + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, totalSum + 1):
                if j >= arr[i - 1]:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        minimumPossibleSum = 0

        for i in range(totalSum // 2, -1, -1):
            if dp[n][i]:
                minimumPossibleSum = i
                break

        return abs(totalSum - 2 * minimumPossibleSum)
