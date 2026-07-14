class Solution(object):
    def twoSum(self, nums, target):
        n= len(nums)
        freq_map ={}
        for i in range(0,n):
            remaining = target-nums[i]
            if remaining in freq_map:
                return [freq_map[remaining],i]
            freq_map[nums[i]]=i
        