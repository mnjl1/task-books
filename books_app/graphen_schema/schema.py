import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from books_app import crud, database
# from books_app.models import Author
from sqlalchemy.orm import Session
from books_app.database import get_db
from fastapi import Depends

db = get_db()


class Author(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()


class Query(graphene.ObjectType):
    authors = graphene.List(Author)

    @staticmethod
    def resolve_authors(self, info):
        records = []
        authors = crud.get_authors(db=Session, skip=0)
        print(authors)
        for c in authors:
            records.append({'first_name': c.first_name,
                           'last_name': c.last_name})

        return records
