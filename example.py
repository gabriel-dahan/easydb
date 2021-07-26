import asyncio

from easydb.psql import DatabaseConnection

db = DatabaseConnection(
    "database", 
    "user", 
    "host", 
    "password"
)

async def foo():
    obj = await db.fetchval("SELECT something FROM table WHERE object = $1;", object)
    print(obj)

loop = asyncio.get_event_loop()
loop.run_until_complete(foo())