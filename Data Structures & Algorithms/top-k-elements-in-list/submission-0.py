class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = {}
        # counting occurences of each number
        for num in nums:
            if num not in freq_cnt:
                freq_cnt[num] = 1
            else:
                freq_cnt[num] += 1

        # sort frequencies in desc. order
        sorted_tuples = sorted(freq_cnt.items(), key=lambda x: x[1], reverse=True)
        return [kv[0] for kv in sorted_tuples][:k]
