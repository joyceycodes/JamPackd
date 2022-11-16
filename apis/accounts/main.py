from fastapi import FastAPI
from routers import users


app = FastAPI()


@app.get("/api/test")
def test():
    return "Hello FastAPI"
