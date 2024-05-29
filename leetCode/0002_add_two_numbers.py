# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        head = curr
        carry = 0

        while l1 or l2 or carry:
            first_val = l1.val if l1 != None else 0
            second_val = l2.val if l2 != None else 0
            total_sum = first_val + second_val + carry

            if total_sum >= 10:
                carry = total_sum // 10
                total_sum = total_sum - 10
            else:
                carry = 0

            curr.next = ListNode(total_sum)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next
