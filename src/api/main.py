# src/api/main.py
from fastapi import FastAPI

app = FastAPI(title="MetaSquad Engine")

@app.get("/")
def read_root():
    return {"status": "online", "engine": "MetaSquad Optimizer"}