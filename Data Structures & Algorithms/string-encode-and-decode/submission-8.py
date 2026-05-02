class Solution:

    delim = "`"

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            length = len(word)
            output += self.delim
            output += str(length)
            output += self.delim
            output += word

        print(output)
        return output

    def decode(self, s: str) -> List[str]:

        strs = []
        nums = ""
        read = False
        for idx, char in enumerate(s):
            if char == self.delim and read == False:
                read = True
            elif char == self.delim and read == True:
                read = False
                start = idx+1
                end = int(nums) + idx + 1
                word = s[start:end]
                strs.append(word)
                nums = ""
            elif read == True:
                try:
                    int(char)
                    nums += char
                except Exception:
                    pass
            else:
                continue
        
        print(strs)
        return strs

