from pydantic import BaseModel , EmailStr

class userCreate(BaseModel):
    email :EmailStr
    password:str

class userResponse(BaseModel):
    id:int 
    email:EmailStr

    # Config class to allow instantiation from ORM objects or attribute-style dictionaries
    class Config:
        from_attributes = True
