class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        traversed = []
        for num in nums:
            if num in traversed:
                return True
            traversed.append(num)   
        return False