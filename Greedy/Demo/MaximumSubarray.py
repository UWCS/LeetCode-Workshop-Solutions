class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # OPT is defined around OPT(i) being value of subarray ending in element
        # OPT(i) = max(OPT(i-1) + nums[i], nums[i])

        cMax = nums[0]
        cOPT = nums[0]

        for num in nums[1:]:
            cOPT = max(cOPT + num, num)
            cMax = max(cMax, cOPT)
        
        return cMax