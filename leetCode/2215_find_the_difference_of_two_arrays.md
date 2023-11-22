# 2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

```
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
```

## JavaScript Solution
```js
const findDifference = function(nums1, nums2) {
  const uniqueNums1 = new Set(nums1);
  const uniqueNums2 = new Set(nums2);
  const result1 = [];
  const result2 = [];

  for (const num of nums1) {
    if (!uniqueNums2.has(num)) result1.push(num);
  }
    
  for (const num of nums2) {
    if (!uniqueNums1.has(num)) result2.push(num);
  }

  return [Array.from(new Set(result1)), Array.from(new Set(result2))];
};
```

## Java Solution
```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
  public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
    HashSet<Integer> uniqueNums1 = new HashSet<>();
    HashSet<Integer> uniqueNums2 = new HashSet<>();
    List<Integer> result1 = new ArrayList<>();
    List<Integer> result2 = new ArrayList<>();

    // First add all unique numbers to their respective HashSets
    for (int num : nums1) {
      uniqueNums1.add(num);
    }

    for (int num : nums2) {
      uniqueNums2.add(num);
    }

    // Then add all numbers that are not in the other set to their respective result lists
    for (int num : nums1) {
      if (!uniqueNums2.contains(num)) result1.add(num);
    }

    for (int num : nums2) {
      if (!uniqueNums1.contains(num)) result2.add(num);
    }

    List<List<Integer>> result = new ArrayList<>();
    result.add(new ArrayList<>(new HashSet<>(result1)));
    result.add(new ArrayList<>(new HashSet<>(result2)));

    return result;
  }
}
```

## Python Solution
```py3
class Solution:
  def findDifference(self, nums1, nums2):
    uniqueNums1 = set(nums1)
    uniqueNums2 = set(nums2)

    # List comprehension to add all numbers that are not in the other set to their respective lists
      # essentially means if the `num` in nums1 is not in uniqueNums2, make it a num of result1
    result1 = [num for num in nums1 if num not in uniqueNums2]
    result2 = [num for num in nums2 if num not in uniqueNums1]

    return [list(set(result1)), list(set(result2))]
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)

- Create two sets to store the unique numbers in each array
  - For Java, make sure you add the numbers to the respective HashSets first
- Create two lists to store the numbers that are not in the other array
- Iterate through each array and add the numbers that are not in the other array to their respective lists
- Return the lists as a list of lists
