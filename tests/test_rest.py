import requests

BASE_URL = "http://localhost:5001"

def test_company_overview_api():
    url = f"{BASE_URL}/api/company_overview?symbol=AAPL"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert "response" in data
