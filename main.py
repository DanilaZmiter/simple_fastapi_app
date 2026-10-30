from fastapi import FastAPI
import uvicorn

app = FastAPI()  # initialize fastapi object


@app.get("/root/")  # make view for /root/ endpoint
def root():
    return {"message": "hello root"}  # json format


if __name__ == "__main__":
    # reload for automatic restart of api on Ctrl + S(saving)
    uvicorn.run("main:app", reload=True)
