from fastapi import FastAPI

<<<<<<< HEAD
# from routers import users


app = FastAPI()


=======
app = FastAPI()


>>>>>>> main
@app.get("/api/test")
def test():
    return "Hello FastAPI"
