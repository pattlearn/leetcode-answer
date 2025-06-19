class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_set = set()
        longest = 0
        L = 0
        
        for R in range(len(s)):
            char_R = s[R]
            
            while char_R in char_set:
                char_L = s[L]
                char_set.remove(char_L)
                L += 1
            
            char_set.add(char_R)
            longest = max(longest, R - L + 1)
            
        print(longest)
        return(longest)