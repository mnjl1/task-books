from fastapi import APIRouter
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router_books = APIRouter(
    prefix='/books',
    tags=['books']
)


@router_books.post('/', response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create book without an author.
    Author can be added to book with def book_add_author()
    """
    return crud.create_book(db=db, book=book)


@router_books.get('/', response_model=List[schemas.Book])
def get_books(skip: int = 0, db: Session = Depends(get_db)):
    """
        Display all books
    """
    books = crud.get_books(db, skip=skip)
    return books


@router_books.post('//{id}/{author_id}', response_model=schemas.Book)
def book_add_author(book_id: int, author_id: int, db: Session = Depends(get_db)):
    """
        Add author to book, 
        params: book_id, author_id
    """
    return crud.book_add_author(db, book_id=book_id, author_id=author_id)
