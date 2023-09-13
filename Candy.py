# https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2023-09-13
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = 0
        left = [1]
        right = [1]

        for i in range(1, n):  # Start from index 1 for left-to-right traversal
            if ratings[i] > ratings[i - 1]:
                left.insert(i, left[i - 1] + 1)
            else:
                left.insert(i, 1)

        for i in range(n - 2, -1, -1):  # Start from the second-to-last element for right-to-left traversal
            if ratings[i] > ratings[i + 1]:
                right.insert(0, right[0] + 1)
            else:
                right.insert(0, 1)

        for i in range(n):
            total += max(left[i], right[i])

        return total
