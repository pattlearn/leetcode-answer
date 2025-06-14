from solution import *

class Test_Case:
    def __init__(self, strs, answer):
        self.strs = strs
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.longestCommonPrefix(strs=test_case.strs)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(strs=["flower","flow","flight"], answer="fl")
    case_2 = Test_Case(strs=["dog","racecar","car"], answer="")
    case_3 = Test_Case(strs=[""], answer="")
    case_4 = Test_Case(strs=["", ""], answer="")
    
    cases = [case_1, case_2, case_3, case_4]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)