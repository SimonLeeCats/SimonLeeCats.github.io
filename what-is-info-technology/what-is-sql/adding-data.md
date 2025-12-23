# Adding Data

### Inserting Rows&#x20;

We know what's a database is, but a database scheme is "what describes the structure of each table, and the datatypes that each column of the table can contain."&#x20;

> For example, in our **Movies** table, the values in the _Year_ column must be an Integer, and the values in the _Title_ column must be a String.

It's almost like parameters in Java. You expect the correct type variable.&#x20;

***

When we insert data, we use the INSERT statement. This declares which table to write into, the column, and one or more rows of data. In general, every time you enter a row, you should also expect entering a value for each column.&#x20;

```
Insert statement with values for all columns
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```

Additionally, if you have incomplete data or columns that support default value, we can also specify the column.

```
INSERT INTO mytable
(column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;
```

{% hint style="info" %}
It should be noted that you can't run aggregated functions inside these insert statements.
{% endhint %}

### Updating Rows

To update rows, you would use the UPDATE statement. Similarly you have to specify exactly which table, columns, and rows to update.

```
Update statement with values
UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;

### EXAMPLE ###
UPDATE Movies
SET Title = "Toy Story 3",
    Director = "Lee Unkrich"
WHERE id = 11; 
```

### Deleting Rows

To delete rows, use the DELETE statement.&#x20;

```
Delete statement with condition
DELETE FROM mytable
WHERE condition;
```

{% hint style="danger" %}
If you decide to leave out the `WHERE` constraint, then _all_ rows are removed, which is a quick and easy way to clear out a table completely (if intentional).
{% endhint %}

### Creating Tables

To create a new table:

```
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
```

You can see from this initialization is that there is a clear table scheme. Each column follows a clear data type.

| Data type                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `INTEGER`, `BOOLEAN`                                 | The integer datatypes can store whole integer values like the count of a number or an age. In some implementations, the boolean value is just represented as an integer value of just 0 or 1.                                                                                                                                                                                                                                                                |
| `FLOAT`, `DOUBLE`, `REAL`                            | The floating point datatypes can store more precise numerical data like measurements or fractional values. Different types can be used depending on the floating point precision required for that value.                                                                                                                                                                                                                                                    |
| `CHARACTER(num_chars)`, `VARCHAR(num_chars)`, `TEXT` | <p>The text based datatypes can store strings and text in all sorts of locales. The distinction between the various types generally amount to underlaying efficiency of the database when working with these columns.</p><p>Both the CHARACTER and VARCHAR (variable character) types are specified with the max number of characters that they can store (longer values may be truncated), so can be more efficient to store and query with big tables.</p> |
| `DATE`, `DATETIME`                                   | SQL can also store date and time stamps to keep track of time series and event data. They can be tricky to work with especially when manipulating data across timezones.                                                                                                                                                                                                                                                                                     |
| `BLOB`                                               | Finally, SQL can store binary data in blobs right in the database. These values are often opaque to the database, so you usually have to store them with the right metadata to requery them.                                                                                                                                                                                                                                                                 |

There's also a term called Table constraints. These limit what values can be inserted into that column. Here are a few common constraints.&#x20;

| Constraint           | Description                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PRIMARY KEY`        | This means that the values in this column are unique, and each value can be used to identify a single row in this table.                                                                                                                                                                                                                                                                              |
| `AUTOINCREMENT`      | For integer values, this means that the value is automatically filled in and incremented with each row insertion. Not supported in all databases.                                                                                                                                                                                                                                                     |
| `UNIQUE`             | This means that the values in this column have to be unique, so you can't insert another row with the same value in this column as another row in the table. Differs from the \`PRIMARY KEY\` in that it doesn't have to be a key for a row in the table.                                                                                                                                             |
| `NOT NULL`           | This means that the inserted value can not be \`NULL\`.                                                                                                                                                                                                                                                                                                                                               |
| `CHECK (expression)` | This allows you to run a more complex expression to test whether the values inserted are valid. For example, you can check that values are positive, or greater than a specific size, or start with a certain prefix, etc.                                                                                                                                                                            |
| `FOREIGN KEY`        | <p>This is a consistency check which ensures that each value in this column corresponds to another value in a column in another table.<br><br>For example, if there are two tables, one listing all Employees by ID, and another listing their payroll information, the `FOREIGN KEY` can ensure that every row in the payroll table corresponds to a valid employee in the master Employee list.</p> |

### Altering Tables

What if you want to change your database schema? You can use the statement ALTER TABLE to add, remove, modify, columns/table constraints.

***

To add a column:&#x20;

```
ALTER TABLE mytable
ADD column DataType OptionalTableConstraint 
    DEFAULT default_value;
```

> In some databases like MySQL, you can even specify where to insert the new column using the `FIRST` or `AFTER` clauses, though this is not a standard feature.

This is similar to adding a column in the CREATE TABLE statement.&#x20;

***

To remove a column:&#x20;

```
ALTER TABLE mytable
DROP column_to_be_deleted;
```

***

To rename a table

`ALTER TABLE mytable RENAME TO new_table_name;`

Sometime it's varies with your SQL manager. For an example:

{% embed url="https://dev.mysql.com/doc/refman/8.4/en/alter-table.html" %}

### Dropping Tables

```
DROP TABLE IF EXISTS mytable;
```

{% hint style="info" %}
In addition, if you have another table that is dependent on columns in table you are removing (for example, with a `FOREIGN KEY` dependency) then you will have to either update all dependent tables first to remove the dependent rows or to remove those tables entirely.
{% endhint %}

And that'll be all of the lessons. See you in the exercises.
