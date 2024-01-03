"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
"""

# linked list values
def linked_list_values(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# sum list
def sum_list(head):
    sum = 0
    current = head
    while current:
        sum += current.val
        current = current.next
    return sum

# linked list find
def linked_list_find(head, target):
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False

# get node value
def get_node_value(head, index):
    count = 0
    current = head
    while current:
        if count == index:
            return current.val
        count += 1
        current = current.next

    return None

# reverse list
def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# zipper lists
def zipper_lists(head_1, head_2):
    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0
    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
            tail = tail.next
        else:
            tail.next = current1
            current1 = current1.next
            tail = tail.next
        count += 1
    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2
    
    return head_1

# merge lists
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
    dummy = Node(None)
    tail = dummy
    c1 = head_1
    c2 = head_2
    while c1 and c2:
        if c1.val < c2.val:
            tail.next = c1
            c1 = c1.next
        else:
            tail.next = c2
            c2 = c2.next
        tail = tail.next
    if c1:
        tail.next = c1
    elif c2:
        tail.next = c2

    return dummy.next
    
