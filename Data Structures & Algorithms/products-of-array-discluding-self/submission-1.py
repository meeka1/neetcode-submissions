class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply_internal(subarray):
            product = 1
            for num in subarray:
                product *= num
            return product

        output = [None] * len(nums)
        for i in range(len(output)):
            preInd = multiply_internal(nums[:i]) if i > 0 else 1
            postInd = multiply_internal(nums[i+1:])
            output[i] = preInd * postInd
        return output