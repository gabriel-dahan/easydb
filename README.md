# EasyDB
A module that simplifies connections to databases.

## Install and Import the module :

Installing the module :
```bash
~ git clone https://github.com/gabriel-dahan/python-easydb/
~ cd python-easydb/

# Linux / MacOS
~ python3 -m pip install -U .

# Windows 
~ py -3 -m pip install -U .
```
Importing the module :
```python
from easydb.<db_type> import DatabaseConnection

# Example
from easydb.psql import DatabaseConnection # PostgreSQL support
# or
from easydb import psql # and then psql.DatabaseConnection(...)
```

## Example Code :
```python
import asyncio
from easydb.psql import DatabaseConnection

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