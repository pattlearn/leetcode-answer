from solution import *

class Test_Case:
    def __init__(self, nums, target, answer):
        self.nums = nums
        self.target = target
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.threeSumClosest(nums=test_case.nums, target=test_case.target)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(nums=[-1,2,1,-4], target=1, answer=2)
    case_2 = Test_Case(nums=[0,0,0], target=1, answer=0)
    case_3 = Test_Case(nums=[10,20,30,40,50,60,70,80,90], target=1, answer=60)
    case_4 = Test_Case(nums=[-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38], target=78, answer=77)
    
    cases = [case_1, case_2, case_3, case_4]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)