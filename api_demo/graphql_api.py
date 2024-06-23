import graphene
from flask import Flask
from flask_graphql import GraphQLView

# Sample data
books = [
    {"id": 1, "title": "Python Essentials", "author": "Jane Doe"},
    {"id": 2, "title": "Flask for Beginners", "author": "John Smith"},
]


# Define the Book type
class Book(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    author = graphene.String()


# Define the Query type
class Query(graphene.ObjectType):
    books = graphene.List(Book)
    book = graphene.Field(Book, id=graphene.Int())

    def resolve_books(self, info):
        print(f"Request context: {info.context}")
        print(f"Request headers: {info.context.headers}")
        return books

    def resolve_book(self, info, id):
        return next((book for book in books if book["id"] == id), None)


# Define the Mutation type
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(lambda: Book)

    def mutate(self, info, title, author):
        new_book = {"id": len(books) + 1, "title": title, "author": author}
        books.append(new_book)
        return CreateBook(book=new_book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(lambda: Book)

    def mutate(self, info, id, title=None, author=None):
        book = next((book for book in books if book["id"] == id), None)
        if book:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            return UpdateBook(book=book)
        return UpdateBook(book=None)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(self, info, id):
        global books
        books = [book for book in books if book["id"] != id]
        return DeleteBook(ok=True)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Create the Flask app
app = Flask(__name__)


# Add the GraphQL endpoint
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # Enable the GraphiQL interface
    ),
)

if __name__ == "__main__":
    app.run(debug=True)
