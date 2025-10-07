class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        l = 0
        r = 0

        hS = set()

        while r < len(s):
            while s[r] in hS:
                hS.remove(s[l])
                l += 1
            
            hS.add(s[r])
            
            longest = max(longest, r - l + 1)
            r += 1

        return longest