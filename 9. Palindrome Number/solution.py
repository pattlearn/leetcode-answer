class Solution(object):
    def isPalindrome(self, x:int):
        s = str(x)
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
        # short version but slower and less memory efficient
        # return str(x) == str(x)[::-1]