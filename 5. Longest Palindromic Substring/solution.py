class Solution:
    def longestPalindrome(self, s: str) -> str:
        window = len(s)
        end = 1
        
        while window > 0:
            for i in range(end):
                if s[i:i+window] == s[i:i+window][::-1]:
                    return s[i:i+window]
            end += 1
            window -= 1