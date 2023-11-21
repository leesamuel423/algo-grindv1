# 1378. Replace Employee ID With The Unique Identifier
```
Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.


Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
```

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

The result format is in the following example.

```
Example 1:

Input: 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output: 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation: 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
```

## MySQL / PostgreSQL Solution
```sql
SELECT c.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI c
ON e.id = c.id
```
### Notes
- A LEFT JOIN returns all the rows from the left table (Employees in this case), along with the matching rows from the right table (EmployeeUNI). If there is no match, the result is NULL on the side of the right table.
- The condition used here is e.id = c.id, which means the join is looking for rows where the id field in Employees matches the id field in EmployeeUNI.
## Panda Solution
```py3
# Solution 1
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
  return pd.merge(
    employees, employee_uni, how='left', on='id'
  )[['unique_id', 'name']]
```

```py3
# Solution 2
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
  employees_subset = employees[['id', 'name']]
  employee_uni_subset = employee_uni[['id', 'unique_id']]
  return pd.merge(employees_subset, employee_uni_subset, how='left', on='id')
```
### Notes
- `pd.merge()` is pandas function to merge two DFs.
  - `employees` and `employee_uni` are DFs to be merged
  - `how` specifies type of merge. Left, so all rows from `employees` DF included in results, with matching rows from `employee_uni`. No matches => NaN
  - `on` indicates column on which merge will be based on. Both DFs should have this column, as it is what is used to align the rows
- Solution 2 has memory-efficiency and performance-efficiency if original DFs have many columns that aren't necessary
