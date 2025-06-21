from solution import *

class Test_Case:
    def __init__(self, s, answer):
        self.s = s
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.myAtoi(s=test_case.s)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(s="42", answer=42)
    case_2 = Test_Case(s="   -042", answer=-42)
    case_3 = Test_Case(s="1337c0d3", answer=1337)
    case_4 = Test_Case(s="0-1", answer=0)
    case_5 = Test_Case(s="words and 987", answer=0)
    case_6 = Test_Case(s="-91283472332", answer=-2147483648)
    case_7 = Test_Case(s="", answer=0)
    
    cases = [case_1, case_2, case_3, case_4, case_5, case_6, case_7]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)