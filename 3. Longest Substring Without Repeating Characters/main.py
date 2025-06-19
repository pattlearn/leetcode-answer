from solution import *

class Test_Case:
    def __init__(self, s, answer):
        self.s = s
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s=test_case.s)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(s="abcabcbb", answer=3)
    case_2 = Test_Case(s="bbbbb", answer=1)
    case_3 = Test_Case(s="pwwkew", answer=3)
    case_4 = Test_Case(s="au", answer=2)
    case_5 = Test_Case(s="aab", answer=2)
    case_6 = Test_Case(s="kgquqbcycmqtfkbem", answer=9)
    
    cases = [case_1, case_2, case_3, case_4, case_5, case_6]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)