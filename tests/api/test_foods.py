from fastapi import status
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_create():
    response = client.post(
        "/foods/", json={"name": "Новый продукт", "id_category": 1, "price": 100}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "name": "Новый продукт",
        "description": None,
        "is_special": False,
        "is_vegan": False,
        "id": 10,
        "price": 100,
    }


def test_update():
    response = client.patch(
        "/foods/3",
        json={"name": "Измененный продукт", "description": "Измененный продукт"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "Измененный продукт",
        "description": "Измененный продукт",
        "is_special": False,
        "is_vegan": False,
        "id": 3,
        "price": 100,
    }


def test_delete():
    response = client.delete("/foods/3")
    assert response.status_code == status.HTTP_200_OK


def test_get_by_id():
    response = client.get("/foods/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "Лимонад",
        "description": "Лимонад",
        "is_special": False,
        "is_vegan": True,
        "toppings": ["Киви", "Ананас", "Миндаль"],
        "price": 100,
    }


def test_get():
    response = client.get("/foods/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "name": "Лимонад",
            "description": "Лимонад",
            "is_special": False,
            "is_vegan": True,
            "toppings": ["Киви", "Ананас", "Миндаль"],
            "price": 100,
        },
        {
            "name": "Сок",
            "description": "Сок",
            "is_special": False,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
        {
            "name": "Картошка",
            "description": "Картошка",
            "is_special": False,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
        {
            "name": "Капуста",
            "description": "Капуста",
            "is_special": True,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
        {
            "name": "Бла бла бла",
            "description": "Бла бла бла",
            "is_special": False,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
        {
            "name": "Секрет 2",
            "description": "Секрет 2",
            "is_special": False,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
    ]


def test_get_vegan():
    response = client.get("/foods/?is_vegan=True")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "name": "Лимонад",
            "description": "Лимонад",
            "is_special": False,
            "is_vegan": True,
            "toppings": ["Киви", "Ананас", "Миндаль"],
            "price": 100,
        },
    ]


def test_get_special():
    response = client.get("/foods/?is_special=True")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "name": "Капуста",
            "description": "Капуста",
            "is_special": True,
            "is_vegan": False,
            "toppings": [],
            "price": 100,
        },
    ]
