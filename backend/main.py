from fastapi import FastAPI
import uvicorn
from typing import Union


app = FastAPI(title="AI Fitness Coach")

# @app.include_router()

# @app.setup("startup")
#     create_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}