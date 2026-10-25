class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = str()
        for string in strs:
            encoded_strs += str(len(string)) + ";" + string
        
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = list()
        decoded_str = ""
        ind = 0
        while ind < len(s):
            delim_pos = s.find(";", ind)
            length = int(s[ind:delim_pos])
            start = delim_pos + 1
            decoded_strs.append(s[start:start + length])
            ind = start + length

        return decoded_strs