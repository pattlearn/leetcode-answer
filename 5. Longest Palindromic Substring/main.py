from solution import *

class Test_Case:
    def __init__(self, s, answer):
        self.s = s
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.longestPalindrome(s=test_case.s)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(s="babad", answer="bab")
    case_2 = Test_Case(s="cbbd", answer="bb")
    
    cases = [case_1, case_2]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)