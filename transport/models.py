CONTAINERS = [
    {
        "id": 1,
        "name": "Контейнер 1",
        "description": "Описание контейнера 1",
        "image": "container1.jpg",
        "price": 10_000,
    },
    {
        "id": 2,
        "name": "Контейнер 2",
        "description": "Описание контейнера 2",
        "image": "container2.jpg",
        "price": 20_000,
    },
    {
        "id": 3,
        "name": "Контейнер 3",
        "description": "Описание контейнера 3",
        "image": "container3.jpg",
        "price": 25_000,
    },
]

ORDERS = {
    1: {
        "containers": [1, 3],
        "transport": "Поезд",
    },
    2: {
        "containers": [2],
        "transport": "Самолёт",
    },
}


def collect_cart():
    collected_orders = {}
    for order_id, order in ORDERS.items():
        containers = []
        total_price = 0
        for container in CONTAINERS:
            if container["id"] in order["containers"]:
                containers.append(container)
                total_price += container["price"]
        collected_orders[order_id] = {
            "containers": containers,
            "transport": order["transport"],
            "total_price": total_price,
        }
    return collected_orders