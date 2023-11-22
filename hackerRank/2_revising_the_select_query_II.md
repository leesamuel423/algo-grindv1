# Revising the Select Query II

Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows:

![Alt text](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## MySQL / PostgreSQL Solution
```sql
SELECT name
FROM City
WHERE CountryCode = 'USA' AND population > 120000
```