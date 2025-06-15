# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_linked_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                print("append", list1.val)
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                print("append", list2.val)
                tail.next = list2
                tail = tail.next
                list2 = list2.next
                
        if list1:
            print("append", list1.val)
            tail.next = list1
        if list2:
            print("append", list2.val)
            tail.next = list2

        check = dummy
        while check.next:
            print(f"In ListNode: {check.next.val}")
            check = check.next
        
        
        return dummy.next
    
if __name__ == "__main__":
    dummy = ListNode(val=10)
    tail = dummy
    tail.next = ListNode(val=20)
    tail = tail.next
    tail.next = ListNode(val=30)
    print(dummy.next.next.next.val)