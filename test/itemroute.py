import json

def test_create_item(client):
    data = {"title" : "alifi" , "description" : "i10"}
    response = client.post("/items" , json.dumps(data))
    assert response.status_code==200

def test_get_items(client):
    response = client.get("/items/all" )
    assert response.status_code==200

def test_get_item(client):
    response = client.get("/items/1" )
    assert response.status_code==200
    assert response.json()["title"]=="alifi"

