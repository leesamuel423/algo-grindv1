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
    
# is univalue list
def is_univalue_list(head):
    current = head
    initial_value = current.val 
    while current:
        if current.val != initial_value:
            return False
        current = current.next
    return True

# longest streak
def longest_streak(head):
    if not head:
        return 0
    current = head
    current_val = head.val
    current_streak = 0
    longest_streak = 0

    while current:
        if current.val == current_val:
            current_streak += 1
        else:
            current_streak = 1
            current_val = current.val
        longest_streak = max(longest_streak, current_streak)
        current = current.next  

    return longest_streak

# remove node
def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    
    current = head
    prev = None

    while current:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next

    return head

# insert node
def insert_node(head, value, index):
    new = Node(value)
    if index == 0:
        new.next = head
        return new
    
    current = head
    count = 1

    while current:
        if count == index:
            new.next = current.next
            current.next = new
            break
        current = current.next
        count += 1

    return head

# create linked list
def create_linked_list(values):
    head = Node('start')
    current = head
    for val in values:
        new = Node(val)
        current.next = new
        current = current.next

    return head.next

# add list actual
def add_lists(head_1, head_2):
    c1 = head_1
    c2 = head_2
    dummy = Node(None)
    tail = dummy
    placeholder = 0
    while c1 or c2 or placeholder:
        val1 = 0 if not c1 else c1.val
        val2 = 0 if not c2 else c2.val
        sum = val1 + val2 + placeholder
        placeholder = sum // 10
        new = Node(sum % 10)
        tail.next = new
        tail = tail.next
        if c1:
            c1 = c1.next
        if c2:
            c2 = c2.next
    return dummy.next
