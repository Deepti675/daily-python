https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        # print(nums[-1])
        left,right=0,nums[-1]-nums[0]
        while left<right:
            mid,temp,i=(left+right)//2,0,0
            while i<len(nums)-1 and temp<p:
                if nums[i+1]-nums[i]<=mid:
                    temp,i=(temp+1,i+2)
                else:
                    temp,i=(temp,i+1)
            if temp>=p:
                left,right=(left,mid)
            else:
                left,right=(mid+1,right)
        return left
    
