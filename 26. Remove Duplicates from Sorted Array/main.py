from solution import *

class Test_Case:
    def __init__(self, nums, answer, list_out):
        self.nums = nums
        self.answer = answer
        self.list_out = list_out
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.removeDuplicates(nums=test_case.nums)
    exp_result = test_case.answer
    list_out = test_case.list_out
    
    if (result == exp_result) & (test_case.nums == list_out):
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(nums=[1,1,2], answer=2, list_out=[1,2])
    case_2 = Test_Case(nums=[0,0,1,1,1,2,2,3,3,4], answer=5, list_out=[0,1,2,3,4])
    
    cases = [case_1, case_2]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)