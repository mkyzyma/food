from fastapi import status
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_create():
    response = client.post(
        "/food-categories/",
        json={"name": "Новая категория", "description": "Новая категория"},
    )
    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "id": 4,
        "name": "Новая категория",
        "is_publish": False,
    }


def test_update():
    response = client.patch("/food-categories/2", json={"name": "Измененная категория"})
    print(response.json())

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 2,
        "is_publish": True,
        "name": "Измененная категория",
    }


def test_delete():
    response = client.delete("/food-categories/3")
    assert response.status_code == status.HTTP_200_OK


def test_get_by_id():
    response = client.get("/food-categories/2")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "Гарниры",
        "is_publish": True,
        "id": 2,
        "foods": [
            {
                "name": "Картошка",
                "description": "Картошка",
                "is_special": False,
                "is_vegan": False,
                "id": 4,
                "toppings": [],
            },
            {
                "name": "Капуста",
                "description": "Капуста",
                "is_special": True,
                "is_vegan": False,
                "id": 5,
                "toppings": [],
            },
            {
                "name": "Морковка",
                "description": "Морковка",
                "is_special": False,
                "is_vegan": False,
                "id": 6,
                "toppings": [],
            },
            {
                "name": "Бла бла бла",
                "description": "Бла бла бла",
                "is_special": False,
                "is_vegan": False,
                "id": 7,
                "toppings": [],
            },
        ],
    }


def test_get():
    response = client.get("/food-categories/")
    print(response.json())
    assert response.json() == [
        {
            "name": "Напитки",
            "is_publish": True,
            "id": 1,
            "foods": [
                {
                    "name": "Лимонад",
                    "description": "Лимонад",
                    "is_special": False,
                    "is_vegan": True,
                    "id": 1,
                    "toppings": ["Киви", "Ананас", "Миндаль"],
                },
                {
                    "name": "Сок",
                    "description": "Сок",
                    "is_special": False,
                    "is_vegan": False,
                    "id": 2,
                    "toppings": [],
                },
            ],
        },
        {
            "name": "Гарниры",
            "is_publish": True,
            "id": 2,
            "foods": [
                {
                    "name": "Картошка",
                    "description": "Картошка",
                    "is_special": False,
                    "is_vegan": False,
                    "id": 4,
                    "toppings": [],
                },
                {
                    "name": "Капуста",
                    "description": "Капуста",
                    "is_special": True,
                    "is_vegan": False,
                    "id": 5,
                    "toppings": [],
                },
                {
                    "name": "Бла бла бла",
                    "description": "Бла бла бла",
                    "is_special": False,
                    "is_vegan": False,
                    "id": 7,
                    "toppings": [],
                },
            ],
        },
    ]


def test_get_vegan():
    response = client.get("/food-categories/?is_vegan=True")
    print(response.json())
    assert response.json() == [
        {
            "name": "Напитки",
            "is_publish": True,
            "id": 1,
            "foods": [
                {
                    "name": "Лимонад",
                    "id": 1,
                    "description": "Лимонад",
                    "is_special": False,
                    "is_vegan": True,
                    "toppings": ["Киви", "Ананас", "Миндаль"],
                },
            ],
        },
    ]


def test_get_special():
    response = client.get("/food-categories/?is_special=True")
    print(response.json())
    assert response.json() == [
        {
            "name": "Гарниры",
            "is_publish": True,
            "id": 2,
            "foods": [
                {
                    "name": "Капуста",
                    "id": 5,
                    "description": "Капуста",
                    "is_special": True,
                    "is_vegan": False,
                    "toppings": [],
                },
            ],
        },
    ]
