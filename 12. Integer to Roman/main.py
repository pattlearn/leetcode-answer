from solution import *

class Test_Case:
    def __init__(self, num, answer):
        self.num = num
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.intToRoman(num=test_case.num)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(num=3749, answer="MMMDCCXLIX")
    case_2 = Test_Case(num=58, answer="LVIII")
    case_3 = Test_Case(num=1994, answer="MCMXCIV")
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)