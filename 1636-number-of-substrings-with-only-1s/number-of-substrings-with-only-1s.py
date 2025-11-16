class Solution(object):
    def numSub(self, s):
        mod=10**9+7
        count=0
        result=0
        for c in s:
            if c=="1":
                count+=1
            else:
                result+=count*(count+1)//2
                result%=mod
                count=0
        result+=count*(count+1)//2
        result%=mod
        return result