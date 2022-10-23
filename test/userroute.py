import json

def test_create_user(client):
    data = {"email" : "tanu@gkmit.co" , "password" : "tanu"}
    response = client.post("/users" , json.dumps(data))
    assert response.status_code==200
    assert response.json()["email"] == "tanu@gkmit.co"
    assert response.json()["is_active"] == True

    
