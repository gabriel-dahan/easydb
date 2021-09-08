# PSQL EasyConn
A module that simplifies asynchronous connections to PostgreSQL.

## Install and Import the module :

Installing the module :
```bash
~ git clone https://github.com/gabriel-dahan/psql-easyconn/
~ cd psql-easyconn/

# Linux / MacOS
~ python3 -m pip install -U .

# Windows 
~ py -3 -m pip install -U .
```
Importing the module :
```python
from easypsql.conn import DatabaseConnection
# or
from easypsql import psql # and then psql.DatabaseConnection(...)
```

## Example Code :
```python
import asyncio
from easypsql.conn import DatabaseConnection

conn = DatabaseConnection(
    "database", 
    "user", 
    "host", 
    "password",
    5432 # Default
)

async def foo():
    obj = await conn.fetchval("SELECT something FROM table WHERE object = $1;", object)
    print(obj)

loop = asyncio.get_event_loop()
loop.run_until_complete(foo())
```