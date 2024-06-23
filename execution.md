http://127.0.0.1:5000/graphql

# GraphQL
Query all books
{
  books {
    id
    title
    author
  }
}
Query a single book by ID
{
  book(id: 1) {
    id
    title
    author
  }
}
Add a new book
mutation {
  createBook(title: "GraphQL for Beginners", author: "Alice Johnson") {
    book {
      id
      title
      author
    }
  }
}
Update a book
mutation {
  updateBook(id: 1, title: "Advanced Python Essentials") {
    book {
      id
      title
      author
    }
  }
}
Delete a book
mutation {
  deleteBook(id: 2) {
    ok
  }
}

