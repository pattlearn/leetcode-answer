class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
        else:
            negative = False
        
        
        x = str(abs(x))
        x = int(x[::-1])
        
        if x > (2**31 - 1):
            return 0
        if x < (-2**31):
            return 0
        
        if negative:
            x = -x
        
        return x