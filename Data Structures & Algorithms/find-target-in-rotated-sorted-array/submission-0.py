class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target and nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > target and nums[mid] > nums[l]:
                r = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                return -1
        return -1



# nums = [3,5,6,0,1,2], target = 4