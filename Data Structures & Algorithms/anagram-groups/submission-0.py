from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count_chars = Counter(string)
            count_chars = "".join(
                sorted(
                        [k for k in count_chars]
                    )
                )

            if count_chars in anagrams.keys():
                anagrams[count_chars].append(string)
            else:
                anagrams[count_chars] = [string]
            
        return list(anagrams.values())
