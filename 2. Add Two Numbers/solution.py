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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        complement = 0
        
        while l1 or l2:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            
            num = num1 + num2 + complement
            complement = 0
            
            if num >= 10:
                complement += 1
                num -= 10
                
            tail.next = ListNode(num)
            tail = tail.next
            
        if complement:
            tail.next = ListNode(1)
            complement = 0
        
        return dummy.next