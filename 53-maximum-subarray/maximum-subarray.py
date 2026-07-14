class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        max_sum=float('-inf')
        total=0
        for i in range(n):
            total+=nums[i]
            max_sum=max(max_sum,total)
            if total<0:
                total=0
        return max_sum