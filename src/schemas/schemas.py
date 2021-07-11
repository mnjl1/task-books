from typing import List, Optional
import graphene
from pydantic import BaseModel
from src.models.models import Book as BookModel
from src.models.models import Author as AuthorModel
from graphene_sqlalchemy import SQLAlchemyObjectType


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


class BookSchema(SQLAlchemyObjectType):
    class Meta:
        model = BookModel


class AuthorSchema(SQLAlchemyObjectType):
    class Meta:
        model = AuthorModel


class SearchResult(graphene.Union):
    class Meta:
        types = (BookSchema, AuthorSchema)
