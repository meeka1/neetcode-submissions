class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # w = ind2 - ind1
        # h = min(heights[ind2], heights[ind1])
        # area = w * h

        max_area = 0
        ind1 = 0
        ind2 = len(heights)-1

        while ind1 < ind2:
            w = ind2 - ind1
            if heights[ind2] < heights[ind1]:
                h = heights[ind2]
                ind2 -= 1
            else:
                h = heights[ind1]
                ind1 += 1

            area = w * h
            max_area = max(max_area, area)

        return max_area