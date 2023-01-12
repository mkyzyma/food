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
    }


def test_update():
    response = client.patch("/food-categories/2", json={"name": "Измененная категория"})
    print(response.json())

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 2,
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
        "id": 2,
        "foods": [
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
                "name": "Морковка",
                "description": "Морковка",
                "is_special": False,
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
        ],
    }


def test_get():
    response = client.get("/food-categories/")
    print(response.json())
    assert response.json() == [
        {
            "name": "Напитки",
            "id": 1,
            "foods": [
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
            ],
        },
        {
            "name": "Гарниры",
            "id": 2,
            "foods": [
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
            ],
        },
    ]


def test_get_vegan():
    response = client.get("/food-categories/?is_vegan=True")
    print(response.json())
    assert response.json() == [
        {
            "name": "Напитки",
            "id": 1,
            "foods": [
                {
                    "name": "Лимонад",
                    "description": "Лимонад",
                    "is_special": False,
                    "is_vegan": True,
                    "toppings": ["Киви", "Ананас", "Миндаль"],
                    "price": 100,
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
            "id": 2,
            "foods": [
                {
                    "name": "Капуста",
                    "description": "Капуста",
                    "is_special": True,
                    "is_vegan": False,
                    "toppings": [],
                    "price": 100,
                },
            ],
        },
    ]


def test_get_by_toppings():
    response = client.get("/food-categories/?toppings=Ананас")
    print(response.json())
    assert response.json() == [
        {
            "name": "Напитки",
            "id": 1,
            "foods": [
                {
                    "name": "Лимонад",
                    "description": "Лимонад",
                    "is_special": False,
                    "is_vegan": True,
                    "toppings": ["Киви", "Ананас", "Миндаль"],
                    "price": 100,
                }
            ],
        }
    ]
