class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # order doesnt matter => two pointer pattern
        triplets = list()

        for ind in range(len(nums)):
            l = 0
            r = len(nums) - 1
            while l < r:
                if ind == l:
                    l += 1
                    continue
                elif ind == r:
                    r -= 1
                    continue

                if nums[ind] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[ind] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    triplet = sorted([nums[ind], nums[l], nums[r]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l += 1
                    r -= 1
        return triplets
