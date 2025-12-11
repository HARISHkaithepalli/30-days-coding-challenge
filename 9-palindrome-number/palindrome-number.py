class Solution(object):
    def isPalindrome(self, x):
        r=0
        n=x
        sign=-1 if x<0 else 1
        x=abs(x)
        while x:
            d=x%10
            r=r*10+d
            x//=10
        if r==n:
            return True
        else:
            return False