from pydantic import BaseModel

class User(BaseModel):
    plotno: str
    address: str
    city: str
    state: str
    country: str
    pincode: int
    