from sqlalchemy.orm import Session
from src.models import models
from src import schemas


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


def create_book(db: Session, book: models.Book):
    db_book = models.Book(**book.dict())
    db
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def book_add_author(db: Session, book_id: int, author_id: int):
    author_add = get_author(db, author_id)
    book = get_book(db, book_id)
    book_authors = book.authors
    if author_add not in book_authors:
        book_authors.append(author_add)
        setattr(book, 'authors', book_authors)
        db.add(book)
        db.commit()
        db.refresh(book)
    return book
