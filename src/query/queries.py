from src.models.models import Book
import graphene
from src.schemas import schemas


class Query(graphene.ObjectType):

    all_books = graphene.List(schemas.BookSchema)
    all_authors = graphene.List(schemas.AuthorSchema)
    search = graphene.List(schemas.SearchResult, q=graphene.String())

    def resolve_all_books(self, info):
        query = schemas.BookSchema.get_query(info)
        return query.all()

    def resolve_all_authors(self, info):
        query = schemas.AuthorSchema.get_query(info)
        return query.all()
