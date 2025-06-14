class Solution(object):
    def romanToInt(self, s:str):
        roman = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        out = 0
        
        for idx in range(len(s) - 1):
            cur = roman[s[idx]]
            nex = roman[s[idx + 1]]
            
            if cur < nex:
                out -= cur
            else:
                out += cur                
        out += roman[s[-1]]
            
        return out