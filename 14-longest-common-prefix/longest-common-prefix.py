class Solution(object):
    def longestCommonPrefix(self, strs):
        p=strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(p):
                p=p[:-1]
                if p=='':
                    return ''
        return p
        