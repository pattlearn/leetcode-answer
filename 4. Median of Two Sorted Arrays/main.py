from solution import *

class Test_Case:
    def __init__(self, nums1, nums2, answer):
        self.nums1 = nums1
        self.nums2 = nums2
        self.answer = answer
        
def run_test(idx, test_case):
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1=test_case.nums1, nums2=test_case.nums2)
    exp_result = test_case.answer
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(nums1=[1,3], nums2=[2], answer=2.00000)
    case_2 = Test_Case(nums1=[1,2], nums2=[3,4], answer=2.50000)
    case_3 = Test_Case(nums1=[2], nums2=[], answer=2.00000)
    case_4 = Test_Case(nums1=[], nums2=[2,3], answer=2.50000)
    
    cases = [case_1, case_2, case_3, case_4]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)