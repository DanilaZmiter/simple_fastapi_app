from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from src.models.base import BaseORM
from src.core.database import database
from src.views.company import router as company_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as connection:
        await connection.run_sync(BaseORM.metadata.create_all)
        yield
        await connection.close()


app = FastAPI(lifespan=lifespan)  # initialize fastapi object
app.include_router(company_router)


@app.get("/root")  # make view for /root/ endpoint
def root():
    return {"message": "hello root"}  # json format


if __name__ == "__main__":
    # reload for automatic restart of api on Ctrl + S(saving)
    uvicorn.run("main:app", reload=True)
