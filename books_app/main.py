from sqlalchemy import engine
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/authors/', response_model=schemas.Author)
def create_author(auhtor: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
        Create author and write to database
    """
    return crud.create_author(db=db, author=auhtor)


@app.get('/authors/', response_model=List[schemas.Author])
def get_authors(skip: int = 0, db: Session = Depends(get_db)):
    """
        Display all authors
    """
    authors = crud.get_authors(db, skip=skip)
    return authors


@app.get('/authors/{author_id}', response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    """
        Get author by id
    """
    author = crud.get_author(db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail='Author not found')
    return author


@app.post('/books/', response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create book without an author.
    Author can be added to book with def book_add_author()
    """
    return crud.create_book(db=db, book=book)


@app.get('/books/', response_model=List[schemas.Book])
def get_books(skip: int = 0, db: Session = Depends(get_db)):
    """
        Display all books
    """
    books = crud.get_books(db, skip=skip)
    return books


@app.post('/books/{id}/{author_id}', response_model=schemas.Book)
def book_add_author(book_id: int, author_id: int, db: Session = Depends(get_db)):
    """
        Add author to book, 
        params: book_id, author_id
    """
    return crud.book_add_author(db, book_id=book_id, author_id=author_id)
