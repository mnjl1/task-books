from typing import List, Optional
from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    book_name: str


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int
    authors: List[Author] = []

    class Config:
        orm_mode = True