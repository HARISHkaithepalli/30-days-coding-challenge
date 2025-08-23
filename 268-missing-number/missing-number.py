class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        exp_sum=(n*(n+1))//2
        return exp_sum-sum(nums)
        