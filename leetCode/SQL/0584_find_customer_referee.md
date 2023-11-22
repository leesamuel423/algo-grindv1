# 584. Find Customer Referee

Table: `Customer`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+

In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 ```

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.

```
Example 1:

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

## MySQL Solution
```sql
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id is NULL
-- # ALTERNATIVELY
WHERE IFNULL(referee_id, 0) <> 2
```
### Notes
- `IFNULL` Function (specific to MySQL and SQLite)
  - Syntax: `IFNULL(expression, value_if_null)`
  - Purpose: This function checks if the first argument (`expression`) is `NULL`. If it is, then it returns the second argument. If it is not `NULL`, it returns the value of the first argument
- Combining that, for `IFNULL(referee_id, 0) <> 2` means:
  - If `referee_id` is `NULL`, treat it as a `0`
  - Select customers where `referee_id` is not equal to `2` (`<> 2` means `not equal to 2`)
- Might choose the `IFNULL` method because it is more readable and concise, and allows for the flexibility of substituting `NULL` values with a specific default other than `0`

## PostgreSQL Solution
```sql
SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) <> 2
```
### Notes
- `COALESCE` Function is same as `IFNULL`
  - Use when you want SQL code to be portable across different database systems
  - `COALESCE` can handle more than two arguments and can be used to check multiple expressions/columns

## Panda Solution
```py3
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
  result_df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
  return result_df[['name']]
```
### Notes
- `.isna()` filters for `NaN` values, which is how Pandas represents missing data