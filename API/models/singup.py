from pydantic import BaseModel
class singup(BaseModel):
    Email:str
    Name:str
    Password:str
    City:str