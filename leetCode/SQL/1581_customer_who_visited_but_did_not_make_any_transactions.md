# 1581. Customer Who Visited but Did Not Make Any Transactions
```
Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.
 

Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.
 ```

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

The result format is in the following example.

```
Example 1:

Input: 
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
Output: 
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
Explanation: 
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.
```

## MySQL / PostgreSQL Solution
```sql
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```
### Notes
- `LEFT JOIN` is used to return all rows from the left table, and the matched rows from the right table. The result is NULL from the right side, if there is no match.
- `COUNT()` returns the number of rows that matches a specified criteria, in this case, the number of visits that did not make any transactions (NULL)
- `GROUP BY` is used to group all the rows that have the same `customer_id` together, so that when we apply the `COUNT()` function, it will count the number of visits that did not make any transactions for each customer.

## Panda Solution
```py3
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
  left_merge = visits.merge(transactions, how = 'left', on = 'visit_id')
  filter_Df = left_merge.query('amount.isna()')
  return filter_Df.groupby(['customer_id'])['visit_id'].count().rename('count_no_trans').reset_index()
```
### Notes
- left `merge` visits with transactions on `visit_id`
- `query` for rows where `amount` is `NaN`
- `groupby` customer_id and count the number of visits that did not make any transactions
- `groupby` returns a `Series` object, so we need to use `rename` to rename the column name, and `reset_index` to convert the `Series` object to a `DataFrame` object
  - A `Series` object is a one-dimensional array, similar to a column in a spreadsheet (with a column label). It will assign a row label to each element in the `Series` object. By default, each row label will be assigned an integer value starting from 0.
  - A `DataFrame` object is a two-dimensional array, similar to a spreadsheet or SQL table. It will assign a row label and a column label to each element in the `DataFrame` object. By default, each row label will be assigned an integer value starting from 0, and each column label will be assigned an integer value starting from 0.

  