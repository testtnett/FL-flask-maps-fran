### Postgres DB

A PostgreSQL (Postgres) database and SQLite are both database management systems, but they serve different purposes. PostgreSQL is a robust, open-source relational database designed for handling large and complex data sets, making it suitable for applications with high data volume, multiple users, and advanced features like data integrity and complex queries. On the other hand, SQLite is a lightweight, file-based database primarily used in smaller applications or mobile devices, where simplicity and portability are key. While Postgres offers scalability and advanced functionality, SQLite is more straightforward and self-contained, making it ideal for simpler projects with lower data requirements.

Both databates management systems require an extra extension to handle spatial data (the coordinates we will use to save locations on the map api)

#### Macos

```bash
brew install postgresql@14
```

start postgres
```bash
brew services start postgresql@14
```

stop postgres
```bash
brew services stop postgresql@14
```

to get into the postgres shell
```bash
psql postgres
```

to create a user
```sql
CREATE USER <username> WITH PASSWORD '<password>';
```

to create a database
```sql
CREATE DATABASE <database_name>;
```

to grant privileges to the user
```sql
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;
```

to exit the postgres shell
```sql
\q
```

to login to the postgres shell as the user
```bash
psql -d <database_name> -U <username>
```

to list all databases
```sql
\l
```

to list all tables

```sql
\dt
```

to list all users

```sql
\du
```

to list all schemas

```sql
\dn
```

to list all functions

```sql
\df
```

```sql
\c <database_name> to connect to a database
```

install postgis

```bash
brew install postgis
```

to create a postgis extension

```sql
CREATE EXTENSION postgis;
```

set postgress URI in terminal, do this every time you run the app
`export DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>`
set google maps api in terminal do this every time you run the app
`export GOOGLE_MAPS_API_KEY=<api_key>`
