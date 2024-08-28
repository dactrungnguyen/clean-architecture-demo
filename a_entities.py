class Item:
    def __init__(self, name: str, price: float, quantity: int, currency: str) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.currency = currency

class Order:
    def __init__(self, order_id: int, items: list[Item]) -> None:
        self.order_id = order_id
        self.items = items
        self.status = "pending"

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
