from solution import *

class Test_Case:
    def __init__(self, height, answer):
        self.height = height
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.maxArea(height=test_case.height)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(height=[1,8,6,2,5,4,8,3,7], answer=49)
    case_2 = Test_Case(height=[1,1], answer=1)
    
    cases = [case_1, case_2]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)