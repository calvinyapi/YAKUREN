import uvicorn
from fastapi import FastAPI

from Model import Product
from utils import list_product, create_client

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/list/products")
def product_list():
    return list_product()


@app.post("/order/products")
def order_client(id_user: int, id_product: int, quantity: int, status):
    return order_client(id_user, id_product, quantity, status)


@app.put("/add/products")
def create_product(data: Product):
    return create_product(data)


@app.put("/create/clients")
def create_client(lastname: str, firstname: str, age: int, email: str, id_user_type: int):
    return create_client(lastname, firstname, age, email, id_user_type)


if __name__ == "__main__":
    uvicorn.run(app, port=8010)
