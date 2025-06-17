from solution import *

class Test_Case:
    def __init__(self, l1, l2, answer):
        self.l1 = l1
        self.l2 = l2
        self.answer = answer
        
def linked_list_to_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_test(idx, test_case):
    solution = Solution()
    result = solution.addTwoNumbers(
        l1=test_case.l1,
        l2=test_case.l2
    )
    exp_result = test_case.answer
    
    result = linked_list_to_list(result)
    exp_result = linked_list_to_list(exp_result)
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")
        
if __name__ == "__main__":
    print("RESULT")
    case_1 = Test_Case(
        l1=build_linked_list([2,4,3]),
        l2=build_linked_list([5,6,4]),
        answer=build_linked_list([7,0,8])
    )
    case_2 = Test_Case(
        l1=build_linked_list([0]),
        l2=build_linked_list([0]),
        answer=build_linked_list([0])
    )
    case_3 = Test_Case(
        l1=build_linked_list([9,9,9,9,9,9,9]),
        l2=build_linked_list([9,9,9,9]),
        answer=build_linked_list([8,9,9,9,0,0,0,1])
    )
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)