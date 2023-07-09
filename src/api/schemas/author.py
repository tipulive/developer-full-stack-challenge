from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    id: int

class AuthorRead(AuthorBase):
    id: int

class AuthorDelete(BaseModel):
    id: int
