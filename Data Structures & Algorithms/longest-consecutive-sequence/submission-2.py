class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique_nums = list(set(sorted(nums)))

        length = 1
        for i in range(1, len(unique_nums)):
            if unique_nums[i] - unique_nums[i-1] == 1:
                length += 1
            
        return length