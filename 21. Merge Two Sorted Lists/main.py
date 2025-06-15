from solution import *

class Test_Case:
    def __init__(self, list1, list2, answer):
        self.list1 = list1
        self.list2 = list2
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
    result = solution.mergeTwoLists(
        list1=test_case.list1,
        list2=test_case.list2
    )
    exp_result = test_case.answer
    
    result = linked_list_to_list(result)
    exp_result = linked_list_to_list(exp_result)
    
    if result == exp_result:
        print(f"Case_{idx+1} status : Passed")
    else:
        print(f"Case_{idx+1} status : Failed")

if __name__ == "__main__":
    print("RESULTS")
    case_1 = Test_Case(
    list1=build_linked_list([1, 2, 4]),
    list2=build_linked_list([1, 3, 4]),
    answer=build_linked_list([1, 1, 2, 3, 4, 4])
)

    case_2 = Test_Case(
    list1=build_linked_list([]),
    list2=build_linked_list([]),
    answer=build_linked_list([])
)

    case_3 = Test_Case(
    list1=build_linked_list([]),
    list2=build_linked_list([0]),
    answer=build_linked_list([0])
)
    
    cases = [case_1, case_2, case_3]
    
    for idx, case in enumerate(cases):
        run_test(idx, test_case=case)