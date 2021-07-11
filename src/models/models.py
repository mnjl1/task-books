from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.database import Base

author_book = Table('authorbook', Base.metadata,
                    Column('author_id', Integer, ForeignKey('authors.id')),
                    Column('book_id', Integer, ForeignKey('books.id'))
                    )


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship(
        'Book',
        secondary=author_book,
        back_populates='authors'
    )

    def coutBooks(self):
        return len(self.books)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    authors = relationship(
        'Author',
        secondary=author_book,
        back_populates='books'
    )
