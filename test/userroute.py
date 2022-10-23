import json

def test_create_user(client):
    data = {"email" : "ras@gkmit.co" , "password" : "raj"}
    response = client.post("/users" , json.dumps(data))
    assert response.status_code==200
    assert response.json()["email"] == "ras@gkmit.co"
    assert response.json()["is_active"] == True

    
