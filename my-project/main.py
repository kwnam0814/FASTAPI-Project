from fastapi import FastAPI
from mysite.post_api import router as post_router

app = FastAPI()

app.include_router(post_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return "Hello World!"
