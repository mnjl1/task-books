from sqlalchemy.orm import Session
from . import models, schemas


def get_author(db: Session, author_id: int):
    """
        Get author by id
    """
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0):
    """
        Get all authors
    """
    return db.query(models.Author).offset(skip).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        first_name=author.first_name,
        last_name=author.last_name
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_books(db: Session, skip: int = 0):
    """
        Get all books
    """
    return db.query(models.Book).offset(skip).all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_author_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(**book.dict(), author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
