import json

def test_create_user(client):
    data = {"title" : "laptop" , "description" : "i9"}
    response = client.post("/items" , json.dumps(data))
    assert response.status_code==200
    