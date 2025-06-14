from solution import *

class Test_Case:
    def __init__(self, x, answer):
        self.x = x
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.isPalindrome(x=test_case.x)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(x=121, answer=True)
    case_2 = Test_Case(x=-121, answer=False)
    case_3 = Test_Case(x=10, answer=False)
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)