from fastapi import FastAPI
from dotzen import config

app = FastAPI()
username = config("username")

@app.get("/")
def home():
  return {
    "username": username
  }
