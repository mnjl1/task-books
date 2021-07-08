from sqlalchemy import engine
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .routers import authors, books

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Books.ly', description='APIs for autors and books')
app.include_router(authors.router_authors)
app.include_router(books.router_books)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
