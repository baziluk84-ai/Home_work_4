from dataclasses import dataclass, asdict
from typing import List
import json

# Датакласи
@dataclass
class Address:
    country: str
    city: str
    stree: str
    house_number: int
    apartment: int


@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int

@dataclass
class UserOrder:
    user_id: int
    username: str
    address: Address
    items: List[OrderItem]

#Список об'єктів класу UserOrder
orders = [
    UserOrder(
        user_id=1,
        username="Dmytro",
        address=Address(country="Ukraine", city = "Kyev", stree = "Khreshchatyk", house_number = 2, apartment=100),
        items = [
            OrderItem(
                name = "Notebook", price= 145.80, quantity = 2),
            OrderItem(
                name = "Pencils", price= 250.00, quantity = 1)
        ]
    ),
    UserOrder(
        user_id=2,
        username="Oksana",
        address=Address(country="Ukraine", city = "Rivne", stree = "Kyivska", house_number = 33, apartment=15),
        items = [
            OrderItem(name = "Drawing album", price = 300.00, quantity = 1),
            OrderItem(name = "Gouache", price = 100.00, quantity = 1),
        ]

    ),
]

#Серіалізація списку в JSON та запис у файл
order_dict = [asdict(order) for order in orders]

with open("orders.json", 'w') as f:
    json.dump(order_dict, f, indent=4)

#Читання з файлу
with open("orders.json") as f:
    data = json.load(f)


#Десеріалізація назад у список UserOrder
load_from_file = []

for item in data:
    address = Address(**item["address"])
    items = [OrderItem(**product) for product in item["items"]]

    user_order =UserOrder(
        user_id=item["user_id"],
        username=item["username"],
        address=address,
        items=items
    )

    load_from_file.append(user_order)

#Виведення кожного об’єкта в окремому рядку
for order in load_from_file:
    print(order)