from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username: str =Field(..., min_length=4, max_length=16)
    password: str = Field(..., min_length=6)

class UserCreate(UserBase):
    pass

class UserLogin(UserBase):
    pass
