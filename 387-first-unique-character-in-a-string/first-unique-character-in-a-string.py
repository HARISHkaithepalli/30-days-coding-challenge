class Solution(object):
    def firstUniqChar(self, s):
        freq=[0]*26
        for c in s:
            index=ord(c)-ord('a')
            freq[index]+=1

        for i,c in enumerate(s):
            index=ord(c)-ord('a')
            if freq[index]==1:
                return i

        return -1
        