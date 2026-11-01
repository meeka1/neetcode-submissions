class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_nums = sorted(list(set(nums)))

        length = 1
        max_length = 1
        for i in range(1, len(unique_nums)):
            if abs(unique_nums[i] - unique_nums[i-1]) == 1:
                length += 1
            else:
                length = 1
            max_length = max(max_length, length)
            
        return max_length