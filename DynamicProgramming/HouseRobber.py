class Solution:
    def rob(self, nums: List[int]) -> int:
        # OPT[i] = max(nums[i] + OPT[i+2], OPT[i+1])
        opt = [None] * (len(nums) + 1)

        opt[-1] = 0
        opt[-2] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            opt[i] = max(nums[i] + opt[i+2], opt[i+1])
        
        return opt[0]