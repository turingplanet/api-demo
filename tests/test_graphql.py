import requests

GRAPHQL_URL = "http://localhost:5001/graphql"

def test_graphql_get_users():
    query = """
    {
        posts {
            id
        }
    }
    """
    response = requests.post(GRAPHQL_URL, json={'query': query})
    assert response.status_code == 200
    data = response.json()
    assert data is not None