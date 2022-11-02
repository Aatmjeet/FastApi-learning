from typing import Union
from fastapi import FastAPI
from api.api import router
app = FastAPI()


app.include_router(router)


@app.get("/")
async def read_root():
    return {"message": "welcome to root"}

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_name": item.name}
