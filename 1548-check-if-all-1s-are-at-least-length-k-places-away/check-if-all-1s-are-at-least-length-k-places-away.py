class Solution(object):
    def kLengthApart(self, nums, k):
        last_one=-10**9
        for i in range(len(nums)):
            if nums[i]==1:
                if i-last_one-1<k:
                    return False
                last_one=i
        return True
        
        