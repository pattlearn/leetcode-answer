class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        check = {s[0]: 1}
        L = 0
        R = 1
        longest = 1
        
        while R < len(s):
            char_L = s[L]
            char_R = s[R]
            
            if char_R not in check:
                check[char_R] = 1
                if longest < (R - L + 1):
                    longest = R - L + 1
                    print(s[L:(R + 1)])
                R += 1
            else:
                check[char_R] += 1
                
                if check[char_R] > 1:
                    if char_L != char_R:
                        while char_L != char_R:
                            char_L = s[L]
                            char_R = s[R]
                            check[char_L] -= 1
                            L += 1
                        R += 1
                    else:
                        check[char_R] -= 1
                        R += 1
                        L += 1
            
                else:
                    if longest < (R - L + 1):
                        longest = R - L + 1
                        print(s[L:(R + 1)])
                    
                    R += 1
        print(longest)
        return longest