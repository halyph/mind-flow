---
tags:
  - postgresql
---

# PostgreSQL

## References

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [Why upgrade PostgreSQL?](https://why-upgrade.depesz.com)
  
### Tools 

- [pgx_scripts](https://github.com/pgexperts/pgx_scripts) - A collection of useful little scripts for database analysis and administration
  - [bloat](https://github.com/pgexperts/pgx_scripts/tree/master/bloat) - queries to estimate bloat in *tables* and *indexes*
- [pg_repack](https://github.com/reorg/pg_repack) is a PostgreSQL extension which lets you remove *bloat* from *tables* and *indexes*, and optionally restore the physical order of clustered indexes.

## 1. Export to CSV with `\copy`

??? info "References"

    - PostgreSQL Documentation: [`COPY` — copy data between a file and a table](https://www.postgresql.org/docs/current/sql-copy.html)
    - Atlassian: [Export to CSV with `\copy`](https://www.atlassian.com/data/sql/export-to-csv-from-psql)
    - SO: [Export specific rows from a PostgreSQL table as INSERT SQL script](https://stackoverflow.com/questions/12815496/export-specific-rows-from-a-postgresql-table-as-insert-sql-script/12824831#12824831)
 
```sql title="myquery.sql"
\COPY (SELECT abc FROM tbl_name WHERE <query>) TO 'sample-result.csv' CSV header;
```

```shell
➜ psql -af myquery.sql
```

## 2. Terminating long running connections

If you need to terminate a long running query or a connection e.g. because it is in IDLE in transaction admins can run:

```sql
select user_management.terminate_backend(<pid>);
```

Or to terminate all application connections:

```sql
select user_management.terminate_backend(pid)
  from pg_stat_activity
 where usename = 'your_application_user';
```

or use `pg_terminate_backend ( pid integer ) → boolean` sends SIGTERM signal to backend processes identified by process ID [^1]

[^1]: Terminates the session whose backend process has the specified process ID. This is also allowed if the calling role is a member of the role whose backend is being terminated or the calling role has been granted pg_signal_backend, however only superusers can terminate superuser backends (see [Server Signaling Functions](https://www.postgresql.org/docs/13/functions-admin.html#FUNCTIONS-ADMIN-SIGNAL))

## 3. Get all ID columns in PSQL

```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND column_name LIKE '%id';
```

??? example

    ```
          column_name      |     data_type
    -----------------------+-------------------
    id                    | integer
    ...
    some_id               | uuid
    id                    | text
    notification_id       | uuid
    (21 rows)
    ```

## 4. List and order tables by size

see SO: [PostgreSQL: Get table size](https://stackoverflow.com/questions/21738408/postgresql-list-and-order-tables-by-size)

This shows you the size of all tables in the schema `pg_catalog`:

```sql
SELECT table_name,
       PG_SIZE_PRETTY(PG_TOTAL_RELATION_SIZE(QUOTE_IDENT(table_name))),
       PG_TOTAL_RELATION_SIZE(QUOTE_IDENT(table_name))
FROM information_schema.tables
WHERE table_schema = 'pg_catalog'
ORDER BY 3 DESC;
```

??? example

    | table\_name | pg\_size\_pretty | pg\_total\_relation\_size |
    | :--- | :--- | :--- |
    | pg\_proc | 1320 kB | 1351680 |
    | pg\_attribute | 856 kB | 876544 |
    | pg\_rewrite | 776 kB | 794624 |

This shows you the size of all tables in all schemas:

```sql
SELECT table_schema,
       table_name,
       PG_RELATION_SIZE('"' || table_schema || '"."' || table_name || '"')
FROM information_schema.tables
ORDER BY 3 DESC;
```

??? example

    | table\_schema | table\_name | pg\_relation\_size |
    | :--- | :--- | :--- |
    | pg\_catalog | pg\_proc | 884736 |
    | public | content\_production\_briefings | 688128 |
    | pg\_catalog | pg\_attribute | 573440 |
    | pg\_catalog | pg\_collation | 114688 |
    | information\_schema | sql\_features | 65536 |
    | pg\_catalog | pg\_amop | 57344 |
