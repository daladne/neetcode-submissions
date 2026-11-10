class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = ""
        res = ""
        lens += str(len(strs)) + " "

        for s in strs:  
            lens += str(len(s)) + " "
            res += s
        
        res = lens + res
        
        return res
            

    def decode(self, s: str) -> List[str]:
        count = None
        lens = []
        strs = []
        temp = ""
        start = ""

        for i, c in enumerate(s):
            if c != " ":
                temp += c
            else:
                if count == None:
                    count = int(temp)
                else:
                    lens.append(int(temp))
                
                temp = ""
                if len(lens) == count: 
                    start = i + 1
                    break

        for length in lens:
            strs.append(s[start:start + length])
            start += length

        return strs
        

            