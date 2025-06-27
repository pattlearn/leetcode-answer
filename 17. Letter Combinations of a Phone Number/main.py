from solution import *

class Test_Case:
    def __init__(self, digits, answer):
        self.digits = digits
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.letterCombinations(digits=test_case.digits)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(digits="23", answer=["ad","ae","af","bd","be","bf","cd","ce","cf"])
    case_2 = Test_Case(digits="", answer=[])
    case_3 = Test_Case(digits="2", answer=["a","b","c"])
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)