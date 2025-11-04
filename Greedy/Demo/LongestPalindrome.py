class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}

        for char in s:
            hm[char] = hm.get(char,0) + 1

        total = 0
        hasOdd = False

        for k,f in hm.items():
            if (f % 2) == 0:
                total += f
            elif not hasOdd:
                total += f
                hasOdd = True
            else:
                total += (f - 1)
        
        return total