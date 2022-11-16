from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Playlist(BaseModel):
    name: str
