from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.core.database import database
from src.views.company import router as company_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as connection:
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
