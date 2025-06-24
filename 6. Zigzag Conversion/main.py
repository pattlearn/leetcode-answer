from solution import *

class Test_Case:
    def __init__(self, s, numRows, answer):
        self.s = s
        self.numRows = numRows
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.convert(s=test_case.s, numRows=test_case.numRows)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(s = "PAYPALISHIRING", numRows = 3, answer="PAHNAPLSIIGYIR")
    case_2 = Test_Case(s = "PAYPALISHIRING", numRows = 4, answer="PINALSIGYAHRPI")
    case_3 = Test_Case(s = "A", numRows = 4, answer="A")
    case_4 = Test_Case(s = "AB", numRows = 1, answer="AB")
    cases = [case_1, case_2, case_3, case_4]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)