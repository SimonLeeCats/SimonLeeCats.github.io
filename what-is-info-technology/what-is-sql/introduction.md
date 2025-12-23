# Introduction

To preface this, I'll be using the following materials to learn:&#x20;

{% embed url="https://sqlbolt.com/" %}

{% embed url="https://sqlzoo.net/wiki/SQL_Tutorial" %}

Some times I'll be directly quoting from the text itself and some of the writing will be myself. Since SQL is an fairly easy language, I won't go too depth in some subjects or write it all myself.&#x20;

***

### Relational Databases

A relational database is like a table or an excel spreadsheet. There's a fixed number of columns and an unlimited amount of rows.&#x20;

| Id | Make/Model        | # Wheels | # Doors | Type       |
| -- | ----------------- | -------- | ------- | ---------- |
| 1  | Ford Focus        | 4        | 4       | Sedan      |
| 2  | Tesla Roadster    | 4        | 2       | Sports     |
| 3  | Kawakasi Ninja    | 2        | 0       | Motorcycle |
| 4  | McLaren Formula 1 | 4        | 0       | Race       |
| 5  | Tesla S           | 4        | 4       | Sedan      |

### Select Queries&#x20;

To retrieve data from a database (which contains all the tables), we need select statements. This selection from a database is called a query. A query is a statement which declares what/where is the data.

```
#### Select query for a specific columns
SELECT column, another_column, …
FROM mytable;
```

{% hint style="info" %}
If you do SELECT \*, it retrieves all the columns. Also keep in mind SQL is not whitespace sensitive &#x20;
{% endhint %}

### Queries with Constraints&#x20;

if we had a table with hundreds of millions of data, reading through the rows would be greatly inefficient, hence we use the WHERE clause to filter in the query. Imagine it as like a IF statement.&#x20;

```
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```

Additionally here are some more operators.&#x20;

| Operator            | Condition                                            | SQL Example                    |
| ------------------- | ---------------------------------------------------- | ------------------------------ |
| =, !=, <, <=, >, >= | Standard numerical operators                         | col\_name != 4                 |
| BETWEEN … AND …     | Number is within range of two values (inclusive)     | col\_name BETWEEN 1.5 AND 10.5 |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | col\_name NOT BETWEEN 1 AND 10 |
| IN (…)              | Number exists in a list                              | col\_name IN (2, 4, 6)         |
| NOT IN (…)          | Number does not exist in a list                      | col\_name NOT IN (1, 3, 5)     |

Example:&#x20;

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

How would we solve the first and second ? The answer ended up being:

```
SELECT id, title FROM movies 
WHERE id = 6;
```

Notice how there's only 1 semicolon? Each semicolon is for one query.&#x20;

To solve the second:&#x20;

```
SELECT title, year FROM movies
WHERE year BETWEEN 2000 AND 2010;
```

### Queries with constraints (Pt 2)

For strings operators "operate" a little differently:

| =          | Case sensitive exact string comparison (_notice the single equals_)                                   | col\_name = "abc"                                                            |
| ---------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| != or <>   | Case sensitive exact string inequality comparison                                                     | col\_name != "abcd"                                                          |
| LIKE       | Case insensitive exact string comparison                                                              | col\_name LIKE "ABC"                                                         |
| NOT LIKE   | Case insensitive exact string inequality comparison                                                   | col\_name NOT LIKE "ABCD"                                                    |
| %          | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | <p>col_name LIKE "%AT%"<br>(matches "AT", "ATTIC", "CAT" or even "BATS")</p> |
| \_         | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)                    | <p>col_name LIKE "AN_"<br>(matches "AND", but not "AN")</p>                  |
| IN (…)     | String exists in a list                                                                               | col\_name IN ("A", "B", "C")                                                 |
| NOT IN (…) | String does not exist in a list                                                                       | col\_name NOT IN ("D", "E", "F")                                             |

&#x20;"=" compares the string exactly. "LIKE" compares the string with case insensitivity.&#x20;

For example this code would find all WALL-\* movies from a table&#x20;

```
SELECT title, director FROM movies 
WHERE title like "WALL-%";
```

### Filtering and Sorting Queries

It should be mention that sometimes many movies can be released in the same year. Hence, with the "DISTINCT" keyword, it discards rows that have duplicate column values.&#x20;

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

Additionally, sometimes tables aren't ordered. The ORDER BY clause gives a column in ascending or descending order.&#x20;

```
Select query with ordered results
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```

Additionally, if we don't want to return all the rows like by the ORDER BY, we can limit the amount of lines returned or offset (place an starting point)

```
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

For example:

```
SELECT title FROM movies
ORDER BY title ASC
LIMIT 5 OFFSET 5;
```

This would select all rows from the column "Title", order by ascending, and then starting from the 5th, it counts the NEXT 5 movies until the limit. Let's move on to a more realistic challenge.&#x20;

***

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

The answers are below:

```
1: 
SELECT Country, Population, City 
FROM north_american_cities
where Country = "Canada"
2:
SELECT * 
FROM north_american_cities
where Country = "United States"
order by Latitude desc
3:
SELECT * 
FROM north_american_cities
where longitude < -87.629798
order by longitude asc
4:
SELECT * 
FROM north_american_cities
where country LIKE "Mexico"
order by population desc
limit 2
5:
SELECT * 
FROM north_american_cities
where longitude < -87.629798
order by longitude asc
```

See you in the next lessons!&#x20;
