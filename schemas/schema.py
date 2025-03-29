from pydantic import BaseModel
class Bot(BaseModel):
    pregunta: str

class User(BaseModel):
    name: str
    email: str
    edad: int