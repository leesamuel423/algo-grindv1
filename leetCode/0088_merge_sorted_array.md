# 88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

```
Example 1:
  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  Output: [1,2,2,3,5,6]
  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
  Input: nums1 = [1], m = 1, nums2 = [], n = 0
  Output: [1]
  Explanation: The arrays we are merging are [1] and [].
  The result of the merge is [1].

Example 3:
  Input: nums1 = [0], m = 0, nums2 = [1], n = 1
  Output: [1]
  Explanation: The arrays we are merging are [] and [1].
  The result of the merge is [1].
  Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## JavaScript Solution
```js
const merge = (nums1, m, nums2, n) => {
    let p1 = m - 1;
    let p2 = n - 1;
    let i = m + n - 1;

    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[i] = nums1[p1];
            p1--;
        } else {
            nums1[i] = nums2[p2];
            p2--;
        }
        i--;
    }

    // add remaining elements in num2
    while (p2 >= 0) {
        nums1[i] = nums2[p2];
        p2--;
        i--;
    }
};
```

## Java Solution
```java
class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int p1 = m - 1;
    int p2 = n - 1;
    int i = m + n - 1;

    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[i] = nums1[p1];
            p1--;
        } else {
            nums1[i] = nums2[p2];
            p2--;
        }
        i--;
    }

    while (p2 >= 0) {
        nums1[i] = nums2[p2];
        p2--;
        i--;
    }
  }
}
```
### Notes
- In Java, when dealing with arrays,  you are working with reference to original array
  - Any changes you make to the array within a method are reflected in the original method
- The method `merge` is defined with a `void` return type, so nothing is returned

## Python Solution
```py3
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    i = m + n - 1

    while p1 >= 0 and p2 >= 0:
      if nums1[p1] > nums2[p2]:
        nums1[i] = nums1[p1]
        p1 -= 1
      else:
        nums1[i] = nums2[p2]
        p2 -= 1
      i -= 1
    
    while p2 >= 0:
      nums1[i] = nums2[p2]
      p2 -= 1
      i -= 1
```

## Overal Strategy
- Utilize reverse iteration method, starting from end of both input arrays and end of merged array
  - The reverse iteration is key to doing this in-place, as it avoids overwriting elements in nums1 that are yet to be compared 
- Maintain three pointers: one for the current position in the first array (nums1), another for the second array (nums2), and the third for the position in the merged array.
- Iterate backwards through the arrays. Compare elements from nums1 and nums2 starting from their respective ends, placing the larger element in the current position of the merged array.
- If one of the arrays is exhausted (i.e., one of the pointers goes below zero), fill the rest of the merged array with the remaining elements of the other array.
- Perform this operation in-place in nums1, assuming nums1 has enough space to hold the elements of both nums1 and nums2.

- Time Complexity: O(n + m)
- Space Complexity: O(1)