class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = ""
                
        num_3 = num // 1000
        num %= 1000
        num_2 = num // 100
        num %= 100
        num_1 = num // 10
        num %= 10
        num_0 = num // 1

        num_str += "M" * num_3
        
        if num_2 == 9:
            num_str += "CM"
            num_2 = 0
        elif num_2 >= 5:
            num_str += "D"
            num_2 -= 5
        elif num_2 == 4:
            num_str += "CD"
            num_2 = 0
        num_str += "C" * num_2
        
        if num_1 == 9:
            num_str += "XC"
            num_1 = 0
        elif num_1 >= 5:
            num_str += "L"
            num_1 -= 5
        elif num_1 == 4:
            num_str += "XL"
            num_1 = 0
        num_str += "X" * num_1
        
        if num_0 == 9:
            num_str += "IX"
            num_0 = 0
        elif num_0 >= 5:
            num_str += "V"
            num_0 -= 5
        elif num_0 == 4:
            num_str += "IV"
            num_0 = 0
        num_str += "I" * num_0
        
        
        print(num_str)
        return num_str