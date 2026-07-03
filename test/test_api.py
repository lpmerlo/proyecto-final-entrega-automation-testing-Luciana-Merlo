import requests

headers = {
    "x-api-key" : "free_user_3FyDhcLQSVtMAg7w1lJjiDxcJ5L"
}

def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    assert response.status_code == 200

def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"

def test_login_sin_email():
    body = {
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing email or username"

def test_create_user():
    body = {
        "name": "Jose",
        "email": "jose.montezuma@bue.edu.ar",
        "password": "12345*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers,json=body)

    data = response.json()

    assert response.status_code == 201
    
    assert body["email"].count("@") == 1
    assert "*" in body["password"]

    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds() < 1

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2",headers=headers)

    assert response.status_code == 204

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2",headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"