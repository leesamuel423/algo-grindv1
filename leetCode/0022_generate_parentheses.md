# 22. Generate Parenthesis

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
```
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
```

## JavaScript Solution
```js
const generateParenthesis = n => {
    const result = [];
    // helper function to generate parenthesis
    const generate = (slate = '', l, r) => {
        if (l === 0 && r === 0) result.push(slate);

        if (l > 0) generate(slate + '(', l - 1, r);
        if (l < r) generate (slate + ')', l, r - 1);
    }
    generate('', n, n);
    return result;
};
```

## Java Solution
```java
import java.util.List;
import java.util.ArrayList;

class Solution {
  public List<String> generateParenthesis(int n) {
    List<String> result = new ArrayList<>();
    generate(result, "", n, n);
    return result;
  }

  private void generate(List<String> result, String slate, int l, int r) {
    if (l == 0 && r == 0){
      result.add(slate);
      return;
    }

    if (l > 0) generate(result, slate + '(', l - 1, r);
    if (l < r) generate (result, slate + ')', l, r - 1);
  }
}
```
### Notes
- In Java, you can't define a function (`generate`) inside another function (`generateParenthesis`). You have to make `generate` a private method of the class `Solution`.
- There are no default argument values in Java, so you need to explicitly pass all arguments when calling a method.

## Python Solution
```py3
class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def generate(slate = '', l = n, r = n):
      if l == 0 and r == 0:
        result.append(slate)
      if l > 0:
        generate(slate + '(', l - 1, r)
      if l < r:
        generate(slate + ')', l, r - 1)
        
    generate()
    return result
```

## Overall Strategy
- Time Complexity: O(4^n / nsqrt(n)) -> Catalan Number 
- Space Complexity: O(4^n / nsqrt(n)) -> Catalan Number
- Catalan Number: https://en.wikipedia.org/wiki/Catalan_number
- Catalan Number: https://www.youtube.com/watch?v=eoofvKI_Okg

- Initialize an empty array to store the result
- Create a helper function to generate parenthesis DFS style
  - The helper function takes in 3 arguments:
    - slate: a string that represents the current combination of parenthesis
    - l: the number of left parenthesis that can be used
    - r: the number of right parenthesis that can be used
  - Base case: if l and r are both 0, then we have used all the parenthesis, so we add the current combination to the result array
  - Recursive case: 
    - If l is greater than 0, then we can add a left parenthesis to the slate, and decrement l by 1
    - If l is less than r, then we can add a right parenthesis to the slate, and decrement r by 1

- Take it or leave it idea (take '(' or take ')')