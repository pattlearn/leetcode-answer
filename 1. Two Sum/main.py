from solution import *

class Test_Case:
    def __init__(self, nums, target, answer):
        self.nums = nums
        self.target = target
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.twoSum(nums=test_case.nums, target=test_case.target)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(nums=[2, 7, 11, 15], target=9, answer=[0, 1])
    case_2 = Test_Case(nums=[3, 2, 4], target=6, answer=[1, 2])
    case_3 = Test_Case(nums=[3, 3], target=6, answer=[0, 1])
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)