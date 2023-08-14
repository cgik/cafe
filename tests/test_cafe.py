def test_index(api_client):
    response = api_client.get("/health")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "Hello World!"
