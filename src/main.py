import graphene
import uvicorn
from starlette.graphql import GraphQLApp
from sqlalchemy import engine
from typing import List
from fastapi import FastAPI
from .models import models
from src.database import engine
from src.routers import authors, books
from src.graphen_schema.schema import Query


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title='Books.ly',
              description='GraphQL APIs for authors and books')
app.include_router(authors.router_authors)
app.include_router(books.router_books)
app.add_route('/grapgql', GraphQLApp(schema=graphene.Schema(query=Query)))


@app.get('/')
async def root():
    return {'message': 'Books application!'}
