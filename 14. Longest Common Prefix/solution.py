class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        common_pref = ""
        idx = 0
        
        while True:
            if idx >= len(strs[0]):
                return common_pref
            
            pref = strs[0][idx]
            for str in strs:
                if idx >= len(str):
                    return common_pref
                if str[idx] != pref:
                    return common_pref
            common_pref += pref
            idx += 1
            
            if idx >= len(str):
                return common_pref
