# 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

## JavaScript Solution

```js
const maxProfit = function (prices) {
	let min = prices[0];
	let maxProfit = 0;

	for (let i = 0; i < prices.length; i++) {
		if (prices[i] - min > maxProfit) {
			maxProfit = prices[i] - min;
		}
		if (prices[i] < min) min = prices[i];
	}

	return maxProfit < 0 ? 0 : maxProfit;
};
```

## Java Solution

```java
class Solution {
  public int maxProfit(int[] prices) {
    int min = prices[0];
    int maxProfit = 0;

    for (int i = 0; i < prices.length; i++) {
      if (prices[i] - min > maxProfit) {
        maxProfit = prices[i] - min;
      }
      if (prices[i] < min) min = prices[i];
    }

    return maxProfit < 0 ? 0 : maxProfit;
  }
}
```

## Python Solution

```py3
class Solution {
  def maxProfit(self, prices: List[int]) -> int:
    min = prices[0]
    maxProfit = 0

    for i in range(len(prices)):
      if prices[i] - min > maxProfit:
        maxProfit = prices[i] - min
      if prices[i] < min:
        min = prices[i]

    return maxProfit if maxProfit > 0 else 0
}
```

## Overall Strategy

- Time Complexity: O(n)
- Space Complexity: O(1)

- Iterate through the array, keeping track of the minimum value and the maximum profit
- If the current value minus the minimum value is greater than the current maximum profit, update the maximum profit
- If the current value is less than the minimum value, update the minimum value
- Return the maximum profit
