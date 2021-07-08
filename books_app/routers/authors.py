from fastapi import APIRouter
from sqlalchemy import engine
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router_authors = APIRouter(
    prefix='/authors',
    tags=['authors']
)


@router_authors.post('/', response_model=schemas.Author)
def create_author(auhtor: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
        Create author and write to database
    """
    return crud.create_author(db=db, author=auhtor)


@router_authors.get('/', response_model=List[schemas.Author], description='Return all authors')
def get_authors(skip: int = 0, db: Session = Depends(get_db)):
    """
        Display all authors
    """
    authors = crud.get_authors(db, skip=skip)
    return authors


@router_authors.get('//{author_id}', response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    """
        Get author by id
    """
    author = crud.get_author(db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail='Author not found')
    return author