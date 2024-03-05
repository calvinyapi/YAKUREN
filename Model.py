from pydantic import BaseModel


class UserData(BaseModel):
    id_user: int = None
    lastname: str
    firstname: str
    age: int
    email: str
    id_user_type: int


class Product(BaseModel):
    id_product: int = None
    name: str
    price: int
    quantity: int
    status: int #1 = envoyé / 0 = remboursé
