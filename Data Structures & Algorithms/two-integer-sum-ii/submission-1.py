class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # non-decreasing = increasing array of integers
        # one valid solution
        # return [index1, index2]; where index1 + index2 = target; index1 < index2

        # two pointers

        lp, rp = 0, len(numbers)-1

        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1, rp+1]
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
            elif numbers[lp] + numbers[rp] < target:
                lp += 1
