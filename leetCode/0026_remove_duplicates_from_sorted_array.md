# 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.
 
```
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## JavaScript Solution
```js
const removeDuplicates = nums => {
  let pointer1 = 0;
  for (let pointer2 = 1; pointer2 < nums.length; pointer2++) {
    if (nums[pointer1] != nums[pointer2]) {
      pointer1++;
      nums[pointer1] = nums[pointer2];
    }
  }
  return pointer1 + 1;
}
```

## Java Solution
```java
class Solution {
  public int removeDuplicates(int[] nums) {
    int pointer1 = 0;
    for (int pointer2 = 1; pointer2 < nums.length; pointer2++) {
      if (nums[pointer1] != nums[pointer2]) {
        pointer1 ++;
        nums[pointer1] = nums[pointer2];
      }
    }
    return pointer1 + 1;
  }
}
```

## Python Solution
```py3
class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    pointer1 = 0

    for pointer2 in range(1, len(nums)):
      if nums[pointer1] != nums[pointer2]:
        pointer1 += 1
        nums[pointer1] = nums[pointer2]
    return pointer1 + 1
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Initialize two pointers, `pointer1` and `pointer2` to 0 and 1 respectively
- Iterate through the array with `pointer2` and compare the value at `pointer1` to the value at `pointer2`
- If the values are not equal, increment `pointer1` and set the value at `pointer1` to the value at `pointer2`
- Return `pointer1 + 1` because `pointer1` is 0-indexed and we want to return the number of unique elements in the array