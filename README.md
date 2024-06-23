# RESTful and GraphQL API Demonstration

This project demonstrates how to set up RESTful API and GraphQL API using Python 3. Please refer to [this document](https://github.com/turingplanet/python-mongo-demo/tree/main?tab=readme-ov-file#python-mongodb-connection-demo) for MongoDB setup and Poetry setup instructions.

## How to Run This Project

### Sample API Demonstrations

To run the sample GraphQL API:
```
poetry run python3 api_demo/graphql_api.py
```

To run the sample RESTful API:
```
poetry run python3 api_demo/rest_api.py
```

### Stock Data Platform APIs

If you want to trigger backend APIs for the stock data platform project:

```
poetry run python3 stock_api/server.py
```

After running this command:
- RESTful API will be available at `http://127.0.0.1:5001/api/*`
- GraphQL API will be available at `http://127.0.0.1:5001/graphql`

Run the following commands for simple testing 
```
poetry run pytest tests
```

# API Reference

## RESTful API Endpoints

| Endpoint | Method | Description | Parameters | Example |
|----------|--------|-------------|------------|---------|
| `/company_overview` | GET | Retrieve company overview data | `symbol` (optional), `sort_field` (optional), `sort_order` (optional, default "asc"), `limit` (optional, default 10) | `/company_overview?symbol=AAPL` |
| `/cash_flow` | GET | Retrieve cash flow data | `symbol`, `sort_field`, `sort_order` (optional, default "asc") | `/cash_flow?symbol=AAPL&sort_field=fiscalDateEnding&sort_order=desc` |
| `/quarterly_earnings` | GET | Retrieve quarterly earnings data | `symbol`, `sort_field`, `sort_order` (optional, default "asc") | `/quarterly_earnings?symbol=MSFT&sort_field=fiscalDateEnding` |
| `/stock_weekly_data` | GET | Retrieve weekly stock data | `symbol`, `sort_field`, `sort_order` (optional, default "asc") | `/stock_weekly_data?symbol=GOOGL&sort_field=date&sort_order=desc` |
| `/news_sentiment` | GET | Retrieve news sentiment data | `symbol`, `sort_field`, `sort_order` (optional, default "asc") | `/news_sentiment?symbol=TSLA&sort_field=time_published&sort_order=desc` |

## GraphQL API

### Queries

| Query | Description | Parameters | Example |
|-------|-------------|------------|---------|
| `posts` | Retrieve all posts | None | `{ posts { id postTitle content } }` |
| `post` | Retrieve a specific post | `id` (required) | `{ post(id: "123") { postTitle content } }` |
| `comment` | Retrieve a specific comment | `id` (required) | `{ comment(id: "456") { content } }` |
| `posts_by_user` | Retrieve posts by a specific user | `user_id` (required) | `{ postsByUser(userId: "user123") { postTitle } }` |
| `users` | Retrieve all users | None | `{ users { userId displayName } }` |
| `user` | Retrieve a specific user | `id` (required) | `{ user(id: "user123") { displayName email } }` |
| `is_user_registered` | Check if a user is registered | `user_id` or `email` | `{ isUserRegistered(userId: "user123") }` |
| `comments` | Retrieve multiple comments | `ids` (required, list of comment IDs) | `{ comments(ids: ["123", "456"]) { content } }` |

### Mutations

| Mutation | Description | Input | Example |
|----------|-------------|-------|---------|
| `create_post` | Create a new post | `userInfo`, `postDate`, `content`, `postTitle`, `postUrl` (optional) | `mutation { createPost(userInfo: {userId: "user123", userName: "John"}, postDate: "2023-06-23", content: "Hello", postTitle: "My Post", postUrl: "test.com") { post { id } } }` |
| `create_comment` | Create a new comment | `userInfo`, `content`, `targetId`, `postId` | `mutation { createComment(userInfo: {userId: "user123", userName: "John"}, content: "Great post!", targetId: "post123", postId: "post123") { comment { id } } }` |
| `upvote_post` | Upvote a post | `post_id` | `mutation { upvotePost(postId: "post123") { post { upvote } } }` |
| `downvote_post` | Downvote a post | `post_id` | `mutation { downvotePost(postId: "post123") { post { downvote } } }` |
| `register_user` | Register a new user | `user_id`, `email`, `display_name`, `password` | `mutation { registerUser(userId: "user123", email: "user@example.com", displayName: "John Doe", password: "securepass") { user { userId } } }` |
| `login` | User login | `user_id`, `password` | `mutation { login(userId: "user123", password: "securepass") { success } }` |
| `delete_post` | Delete a post | `post_id`, `user_id` | `mutation { deletePost(postId: "post123", userId: "user123") { success } }` |


