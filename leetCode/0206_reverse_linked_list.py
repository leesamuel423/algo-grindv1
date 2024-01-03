# 206. Reverse Linked List
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

current # will later be incremented
prev = null


while current:
    next
    current point to previous node
    previous is reassigned to be the current
    current = next


1 -> 2 -> 3 -> null

null <-1        2 -> 3 -> null
p      p       p    c
"""

def reverseList(self, head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev



