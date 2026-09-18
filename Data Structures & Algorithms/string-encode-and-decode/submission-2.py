class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))
            encoded_string += '#'
            encoded_string += string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        string = ""
        start = False
        length = 0
        i = 0
        while i < len(s):
            c = s[i]
            if start == False:
                if c == '#':
                    length = int(string)
                    string = ""
                    if length == 0:
                        decoded_strs.append("")
                    else:
                        start = True
                else:
                    string += c
            else:
                string += c
                length -= 1
                if length == 0:
                    start = False
                    decoded_strs.append(string)
                    string = ""
            i += 1
        return decoded_strs
            
            


