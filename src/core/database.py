from asyncio import current_task

from src.core.settings import settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)


class Database:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=False
        )

    async def get_session(self):
        async with self.session_maker() as session:
            yield session
            await session.close()  # getter for simple session

    async def get_scope_session(self):
        session = async_scoped_session(
            session_factory=self.session_maker,
            scopefunc=current_task,  # asyncio gives current task of app
        )
        yield session
        await session.remove()  # getter for scoped session


database = Database(url=settings.db.url, echo=settings.db.echo)
