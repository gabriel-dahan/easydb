import asyncpg
import asyncio

class PSQLConnection:

    def __init__(self, database, user, host, password, port = 5432):
        self._database = database
        self._user = user
        self._host = host
        self._password = password
        self._port = port

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._initialize())

    async def _initialize(self):
        self.pool = await asyncpg.create_pool(
            database = self._database,
            user = self._user,
            password = self._password,
            host = self._host,
            port = self._port
        )
    
    async def execute(self, query: str, *argv):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute(query, *argv)
    
    async def fetch(self, query: str, *argv):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetch(query, *argv)
    
    async def fetchrow(self, query: str, *argv):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetchrow(query, *argv)

    async def fetchval(self, query: str, *argv):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetchval(query, *argv)