from pydantic import BaseModel

class BookBase(BaseModel):
    name: str
    author_id:int
    pages: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    id: int

class BookRead(BookBase):
    id: int

class BookDelete(BaseModel):
    id: int
