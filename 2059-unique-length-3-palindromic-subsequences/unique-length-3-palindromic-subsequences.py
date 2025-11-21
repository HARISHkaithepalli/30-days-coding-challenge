class Solution(object):
    def countPalindromicSubsequence(self, s):
        n = len(s)
        # first[i]  = first index of chr(i + 'a') in s
        # last[i]   = last  index of chr(i + 'a') in s
        first = [n] * 26
        last  = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        ans = 0
        # Consider each character as the outer char of palindrome: x ? x
        for c in range(26):
            if first[c] < last[c]:  # we have at least two of this char
                seen_middle = set()
                # count distinct middle characters between first and last
                for k in range(first[c] + 1, last[c]):
                    seen_middle.add(s[k])
                ans += len(seen_middle)

        return ans
        
        