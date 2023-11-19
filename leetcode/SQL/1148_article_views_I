# 1148. Article Views I

Table: Views
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
```

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

```
Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

## MySQL / PostgreSQL Solution
```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
```
### Notes
- `DISTINCT` keyword to get unique
- Specify order with `ORDER BY`

## Panda Solution
```py3
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
  viewed_own = views[views['author_id'] == views['viewer_id']]
  unique_authors = sorted(viewed_own['author_id'].unique())
  result_df = pd.DataFrame({'id': unique_authors})
  return result_df
```
### Notes
- `viewed_own` filters for only rows where `author_id` and `viewer_id` are the same
- `unique_authors` finds unique values of the `viewed_own` and sorts it. 
  - return type of `.unique()` is NumPy array
  - return type of `sorted()` is a new list (takes an iterablye like a NumPy array and sorts it in ascending order by default)
- for `result_df`, create a new dataframe:
  - Don't modify the original dataframe, allowing for data integrity
  - So a new DataFrame is created with a single column named `id`, with data coming from the `unique_authors` list
