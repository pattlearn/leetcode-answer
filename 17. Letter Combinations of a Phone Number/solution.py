class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        __dict__ = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        output = []
        if len(digits) == 0:
            return output
        
        def backtrack(index, current_combination):
            
            if index == len(digits):
                output.append("".join(current_combination))
                return
            
            digit = digits[index]
            letters = __dict__[digit]
            
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
        
        backtrack(0, [])
        return output