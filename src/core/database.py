from src.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Database:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=False
        )

    async def get_session(self):
        async with self.session_maker() as session:
            yield session


database = Database(url=settings.db.url, echo=settings.db.echo)
