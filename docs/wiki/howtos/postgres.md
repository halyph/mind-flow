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