class Solution:
    def isValid(self, s: str) -> bool:
        out = ""
        paren = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        for char in s:
            if char in ["(", "[", "{"]:
                out += char
            else:
                if len(out) == 0:
                    return False
                if char != paren[out[-1]]:
                    return False
                else:
                    out = out[:-1]
        return out == ""