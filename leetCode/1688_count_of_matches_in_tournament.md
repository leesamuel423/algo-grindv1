# 1688. Count of Matches in Tournament

You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

 
```
Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.

Example 2:

Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
```

## JavaScript Solution
```js
const numberOfMatches = function(n) {
  let count = 0;

  const generate = teams => {
    if (teams === 1) return;
    if (teams % 2 === 0) {
        count += (teams / 2);
        generate(teams / 2);
    } else {
        count += (teams - 1) / 2;
        generate((teams - 1) / 2 + 1);
    }
  }

  generate(n);

  return count;
};
```

## Java Solution
```java
class Solution {
  public int numberOfMatches(int n) {
    return generate(0, n);
  }

  public int generate(int count, int teams) {
    if (teams == 1) return count;
    if (teams % 2 == 0) {
      count += (teams / 2);
      return generate(count, teams / 2);
    } else {
      count += (teams - 1) / 2;
      return generate(count, (teams - 1) / 2 + 1);
    }
  }
}
```

## Python Solution
```py3
class Solution:
  def numberOfMatches(self, n: int) -> int:

    def generate(count: int, teams: int) -> int:
      if teams == 1: 
        return count
      if teams % 2 == 0:
        count = count + teams / 2
        return generate(count, teams / 2)
      else:
        count = count + (teams - 1) / 2
        return generate(count, (teams - 1) / 2 + 1)
  
    return int(generate(0, n))

```

## Overall Strategy
- Time Complexity: O(log(n)) -> Each recursive call reduces the number of teams by half
- Space Complexity: O(log(n)) -> Each recursive call adds a new stack frame to the call stack

- Create a recursive function that takes in the current number of matches and the current number of teams
- If the current number of teams is 1, return the current number of matches
- If the current number of teams is even, add the number of teams divided by 2 to the current number of matches and call the function again with the number of teams divided by 2
- If the current number of teams is odd, add the number of teams minus 1 divided by 2 to the current number of matches and call the function again with the number of teams minus 1 divided by 2 plus 1
- Return the result of the recursive function call
