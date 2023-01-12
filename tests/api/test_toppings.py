from fastapi import status
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_create():
    response = client.post("/toppings/", json={"name": "Новый топпинг"})

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id": 4, "name": "Новый топпинг"}


def test_update():
    response = client.patch("/toppings/3", json={"name": "Измененный топпинг"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 3, "name": "Измененный топпинг"}


def test_delete():
    response = client.delete("/toppings/3")
    assert response.status_code == status.HTTP_200_OK


def test_get_by_id():
    response = client.get("/toppings/2")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 2, "name": "Ананас"}


def test_get():
    response = client.get("/toppings/")
    assert response.json() == [
        {"id": 1, "name": "Киви"},
        {"id": 2, "name": "Ананас"},
        {"id": 3, "name": "Миндаль"},
    ]
