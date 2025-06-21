class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if len(s) == 0:
            return 0
        
        num = 0
        negative = False
        
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            negative = False
            s = s[1:]
        elif s[0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return num
        
        num = str(num)
        for n in s:
            if n not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                break
            num += n
            
        num = int(num)
        
        # print(num)
        # print("NEGATIVE,", negative)
        
        if negative:
            return max(-2 ** 31, -num)
        
        return min(num, 2 ** 31 -1 )