# 1757. Recyclable and Low Fat Products

Table: `Products`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+

product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

```
Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
```

## MySQL Solution
```sql
SELECT product_id
FROM product
WHERE low_fats = 'Y' AND recyclable = 'Y'
```

## PostgreSQL
```sql
SELECT product_id
FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y'
```

## Panda Solution
```py3
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
  result_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
  return result_df[['product_id']]
```
OR ALTERNATIVELY
```py3
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query('low_fats == "Y" & recyclable == "Y"')[['product_id']]
```
### Notes
- Filter rows where both low_fats and recyclable is 'Y'
- Select only 'product_id' column from DataFrame and return that