# https://leetcode.com/problems/find-triangular-sum-of-an-array/description/
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while(n>0):
            for i in range(n-1):

                nums[i]=(nums[i]+nums[i+1])%10

            n-=1

        return nums[0]
        
