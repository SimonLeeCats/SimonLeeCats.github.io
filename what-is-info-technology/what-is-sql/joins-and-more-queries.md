# Joins and More Queries

The past few lessons has been centered around an single table. However, what would we do with numerous tables (normalization)&#x20;

> Database normalization is useful because it minimizes duplicate data in any single table, and allows for data in the database to grow independently of each other (ie. Types of car engines can grow independent of each type of car). As a trade-off, queries get slightly more complex since they have to be able to find data from different parts of the database, and performance issues can arise when working with many large table

The problem currently, is that instead of putting all of the data in one big table, sometime databases split it into multiple smaller tables. Hence, you would then use the statement "JOIN" to connect them.  (INNER JOIN and JOIN are the same)

**Example:** Imagine you have two tables:

* **Table 1:** Customer names and their ID numbers
* **Table 2:** Orders and which customer ID placed them

```
SELECT what_you_want
FROM first_table
INNER JOIN second_table
ON first_table.id = second_table.id

###EXAMPLE###
SELECT title, domestic_sales,international_sales FROM movies
INNER JOIN boxoffice 
ON movies.id = boxoffice.Movie_id

SELECT title, rating FROM movies
INNER JOIN boxoffice 
ON movies.id = boxoffice.Movie_id
order by rating desc 
```

### Outer Joins

However, the issue with inner joins that it only shows rows that matches in both rows. In other words, if something exists in one table only, it gets left out completely. The solution is OUTER JOINS, which fill in blanks with NULLS when there is no match.

| JOINS      | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LEFT JOINS | <p></p><p><strong>1. LEFT JOIN</strong></p><ul><li>Keeps ALL rows from the first (left) table</li><li>Adds matching data from the second table where available</li><li>If no match exists, fills in NULL for the second table's columns</li><li></li></ul><p><strong>Example:</strong> Show all customers and their orders (if they have any)</p><ul><li>Result includes customers who haven't ordered anything yet</li></ul> |
| RIGHT JOIN | <p></p><ul><li>Same as LEFT JOIN, but reversed</li><li>Keeps ALL rows from the second (right) table</li><li>Less commonly used (people usually just flip the table order and use LEFT JOIN)</li></ul>                                                                                                                                                                                                                         |
| FULL JOIN  | <p></p><ul><li>Keeps ALL rows from BOTH tables</li><li>Shows everything, whether matched or not</li><li>Most inclusive option</li></ul>                                                                                                                                                                                                                                                                                       |

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Let's go through some examples.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

The 2nd and 3rd one would be:&#x20;

```
SELECT * FROM Buildings;

SELECT DISTINCT building_name, role 
FROM buildings 
  LEFT JOIN employees
    ON building_name = building;
```

### Nulls&#x20;

We should always aim to reduce the amount of NULL values in our database. Sometimes we replace the NULL value with a default value like 0 or empty strings, but sometimes it's not possible to avoid null values. Hence, you can check a column using WHERE clause and the IS NULL / IS NOT NULL constraint.&#x20;

```
SELECT * FROM employees
WHERE Building IS NULL 

# This one finds the name of the buildings that holds no employees
SELECT DISTINCT building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;
```

{% hint style="info" %}
Side Note:&#x20;

SELECT DISTINCT building\_name\
FROM buildings ← This is the LEFT table\
LEFT JOIN employees ← This is the RIGHT table\
ON building\_name = building\
WHERE role IS NULL;
{% endhint %}

### Queries with Expressions&#x20;

Instead of selecting raw columns, you can also use expressions to perform calculations.&#x20;

```
SELECT particle_speed / 2.0 AS half_particle_speed
FROM physics_data
WHERE ABS(particle_position) * 10.0 > 500;
```

However, we don't want to fully incorporate this. If we continue with this, the column's name will be "particle\_speed / 2.0". Instead, we should use the AS statement.&#x20;

```
-- Without AS (confusing column name)
SELECT years_employed * 365;

-- With AS (clear column name)
SELECT years_employed * 365 AS days_employed;
```

An example of this would be:

```
-- Calculate remaining capacity in each building
SELECT 
  building_name,
  capacity,
  COUNT(name) AS employees_assigned,
  capacity - COUNT(name) AS available_spots
FROM buildings
  LEFT JOIN employees ON building_name = building
GROUP BY building_name, capacity;
```

Additionally, you can apply this to naming tables.

```
Example query with both column and table name aliases
SELECT column AS better_column_name, …
FROM a_long_widgets_table_name AS mywidgets
INNER JOIN widget_sales
  ON mywidgets.id = widget_sales.widget_id;
```

{% hint style="info" %}
Also note, you may have saw that sometimes I connected the table name with the column (EX: Buildings.building\_name). If a column name is **unique** (only exists in one table), SQL knows which table you're referring to. However, if the name exist in both, specify them! But of course, usually you would always specify them.

Another note is that SQL doesn't have a strict execution order unlike Python. It executes the SELECT and JOIN first for examples. However, it DOES have an order of execution of an query. We'll go more about this later.&#x20;
{% endhint %}

### Queries with Aggregates

SQL also supports use of aggregate/functions that summarize information about groups of rows. Think of them like methods like len().&#x20;

```
Select query with aggregate functions over all rows
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

Here are the few most common functions:

| Function                                           | Description                                                                                                                                                                                     |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COUNT(**\***)**, **COUNT(**&#x63;olum&#x6E;**)** | A common function used to counts the number of rows in the group if no column name is specified. Otherwise, count the number of rows in the group with non-NULL values in the specified column. |
| **MIN(**&#x63;olum&#x6E;**)**                      | Finds the smallest numerical value in the specified column for all rows in the group.                                                                                                           |
| **MAX(**&#x63;olum&#x6E;**)**                      | Finds the largest numerical value in the specified column for all rows in the group.                                                                                                            |
| **AVG(**&#x63;olumn)                               | Finds the average numerical value in the specified column for all rows in the group.                                                                                                            |
| **SUM(**&#x63;olum&#x6E;**)**                      | Finds the sum of all numerical values in the specified column for the rows in the group.                                                                                                        |

There's more aggregate functions in the document of MySQL

{% embed url="https://dev.mysql.com/doc/refman/8.4/en/built-in-function-reference.html" %}

### Grouped Aggregate Functions

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

The problem with the functions is that it aggregating across all rows. Sometimes, you can instead apply to individual groups of data within that group. Let's create a visual so it's a bit easier to understand.

***

| Student | Score |
| ------- | ----- |
| Alice   | 80    |
| Alice   | 90    |
| Bob     | 70    |
| Bob     | 85    |
| Bob     | 95    |

Imagine you have this table. If you were to do `SELECT AVG(score) FROM students;`

This would return 84. However, we want the average for each student. Hence, when do GROUP BY Student:

| Student | AVG(score) |
| ------- | ---------- |
| Alice   | 85         |
| Bob     | 83.3       |

In other words: "The `GROUP BY` clause works by grouping rows that have the same value in the column specified." Let's do an example.

```
SELECT 
SUM(Years_Employed), Building FROM employees
GROUP BY Building

This solves: "Find the total number of employee years worked in each building"
```

***

One thing is to note the general structure of our queries. The GROUP BY is executed after the WHERE clause, so how do we filter the rows that are groups. Hence, we have the **HAVING** clause.&#x20;

```
SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
FROM mytable
WHERE condition
GROUP BY column
HAVING group_condition;
```

The HAVING clause is specifically paired with the GROUP BY clause, so if you don't need to incorporate this if you don't have the WHERE clause.&#x20;

### Order of Execution of a Query

```
Complete SELECT query
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
    JOIN another_table
      ON mytable.column = another_table.column
    WHERE constraint_expression
    GROUP BY column
    HAVING constraint_expression
    ORDER BY column ASC/DESC
    LIMIT count OFFSET COUNT;
```

The description on SQL Bolt does a good job describing the order, so I'll just copy paste it here.&#x20;

***

### 1. `FROM` and `JOIN`s

The `FROM` clause, and subsequent `JOIN`s are first executed to determine the total working set of data that is being queried. This includes subqueries in this clause, and can cause temporary tables to be created under the hood containing all the columns and rows of the tables being joined.

### 2. `WHERE`

Once we have the total working set of data, the first-pass `WHERE` constraints are applied to the individual rows, and rows that do not satisfy the constraint are discarded. Each of the constraints can only access columns directly from the tables requested in the `FROM` clause. Aliases in the `SELECT` part of the query are not accessible in most databases since they may include expressions dependent on parts of the query that have not yet executed.

### 3. `GROUP BY`

The remaining rows after the `WHERE` constraints are applied are then grouped based on common values in the column specified in the `GROUP BY` clause. As a result of the grouping, there will only be as many rows as there are unique values in that column. Implicitly, this means that you should only need to use this when you have aggregate functions in your query.

### 4. `HAVING`

If the query has a `GROUP BY` clause, then the constraints in the `HAVING` clause are then applied to the grouped rows, discard the grouped rows that don't satisfy the constraint. Like the `WHERE` clause, aliases are also not accessible from this step in most databases.

### 5. `SELECT`

Any expressions in the `SELECT` part of the query are finally computed.

### 6. `DISTINCT`

Of the remaining rows, rows with duplicate values in the column marked as `DISTINCT` will be discarded.

### 7. `ORDER BY`

If an order is specified by the `ORDER BY` clause, the rows are then sorted by the specified data in either ascending or descending order. Since all the expressions in the `SELECT` part of the query have been computed, you can reference aliases in this clause.

### 8. `LIMIT` / `OFFSET`

Finally, the rows that fall outside the range specified by the `LIMIT` and `OFFSET` are discarded, leaving the final set of rows to be returned from the query.

See you in the next lesson about actually adding data now!&#x20;
