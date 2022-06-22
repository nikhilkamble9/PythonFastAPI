from pydantic import BaseModel


class Address(BaseModel):
    address: str
    city: str
    state: str
    pincode: str
