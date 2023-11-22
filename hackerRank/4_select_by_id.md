# Select By ID

Query all columns for a city in CITY with the ID 1661.

The CITY table is described as follows:

![Alt text](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## MySQL / PostgreSQL Solution
```sql
SELECT *
FROM City
WHERE ID = '1661'
```