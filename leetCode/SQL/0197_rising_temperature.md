# 197 Rising Temperature
```
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
This table contains information about the temperature on a certain day.
 ```

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 
```
Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
```

## MySQL / PostgreSQL Solution
```sql
SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1;
```

## Panda Solution
```py3
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
  weather.sort_values(by = 'recordDate', inplace = True)
  return weather[
    (weather.temperature.diff() > 0)
    & (weather.recordDate.diff().dt.days == 1)
    ][['id']]
```
### Notes
- `sort_values` is an in-place operation, so it doesn't return anything.
- inplace argument modifies the DataFrame in place (does not create a new object)
- `diff` is a pandas method that returns the difference between the current and previous row
- `dt.days` is a pandas method that returns the difference in days between the current and previous row
