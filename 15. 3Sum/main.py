from solution import *

class Test_Case:
    def __init__(self, nums, answer):
        self.nums = nums
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.threeSum(nums=test_case.nums)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(nums=[-1,0,1,2,-1,-4], answer=[[-1,-1,2],[-1,0,1]])
    case_2 = Test_Case(nums=[0,1,1], answer=[])
    case_3 = Test_Case(nums=[0,0,0], answer=[[0,0,0]])
    case_4 = Test_Case(nums=[-2,0,1,1,2], answer=[[-2,0,2],[-2,1,1]])
    
    cases = [case_1, case_2, case_3, case_4]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)