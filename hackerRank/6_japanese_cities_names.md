# Japanese Cities' Names

Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

![Alt text](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## MySQL / PostgreSQL Solution
```sql
SELECT name
FROM City
WHERE CountryCode = 'JPN'
```

