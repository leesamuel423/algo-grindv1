# 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

```
Example 1:
![Alt text](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

## JavaScript Solution

```js
const mergeTwoLists = function (list1, list2) {
	const output = new ListNode();
	let current = output;

	let p1 = list1;
	let p2 = list2;

	while (p1 && p2) {
		if (p1.val <= p2.val) {
			current.next = p1;
			p1 = p1.next;
		} else {
			current.next = p2;
			p2 = p2.next;
		}
		current = current.next;
	}

	if (p1) current.next = p1;
	else if (p2) current.next = p2;

	return output.next;
};
```

## Java Solution

```java
class Solution {

  // Definition for singly-linked list.
  public static class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode output = new ListNode(0);
    ListNode current = output;

    ListNode p1 = list1;
    ListNode p2 = list2;

    while (p1 != null && p2 != null) {
      if (p1.val <= p2.val) {
        current.next = p1;
        p1 = p1.next;
      } else {
        current.next = p2;
        p2 = p2.next;
      }
      current = current.next;
    }

    if (p1 != null) current.next = p1;
    else if (p2 != null) current.next = p2;

    return output.next;
  }
}

```

## Python Solution

```py3
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        current = output

        p1 = list1
        p2 = list2

        while p1 and p2:
          if p1.val <= p2.val:
            current.next = p1
            p1 = p1.next
          else:
            current.next = p2
            p2 = p2.next
          current = current.next

        if p1:
          current.next = p1
        elif p2:
          current.next = p2

        return output.next

```

## Overall Strategy

- Time Complexity: O(n)
- Space Complexity: O(1)

- Create a new linked list
- Create a pointer for each list
- While both pointers are not null
  - Compare the values of the pointers
  - Add the smaller value to the new linked list
  - Move the pointer of the smaller value to the next node
- If one pointer is not null
  - Add the rest of the nodes to the new linked list
- Return the new linked list
