# Weather Observation Station 3

Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

The STATION table is described as follows:

![Alt text](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## MySQL / PostgreSQL Solution
```sql
SELECT DISTINCT city
FROM Station
WHERE MOD(id, 2) = 0
-- OR
-- WHERE id % 2 = 0
```