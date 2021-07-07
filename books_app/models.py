from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

from .database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')


# author_book = Table('authorbook', Base.metadata,
#                     Column('authors_id', Integer, ForeignKey('authors.id'),
#                            primary_key=True),
#                     Column('books_id', Integer, ForeignKey('books.id'),
#                            primary_key=True)
#                     )
