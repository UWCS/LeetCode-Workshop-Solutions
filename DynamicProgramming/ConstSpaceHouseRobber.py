class Solution:
    def rob(self, nums: List[int]) -> int:
        # OPT[i] = max(nums[i] + OPT[i+2], OPT[i+1])
        prevprev = 0 
        prev = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            cur = max(nums[i] + prevprev, prev)
            prevprev = prev 
            prev = cur
        
        return prev