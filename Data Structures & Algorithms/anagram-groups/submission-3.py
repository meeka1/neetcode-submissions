from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            count_chars = "".join(sorted(string))
            anagrams[count_chars].append(string)
            
        return list(anagrams.values())
