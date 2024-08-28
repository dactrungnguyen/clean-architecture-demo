from a_entities import Order


class OrderRepository:
    def get_order(self, order_id: int) -> Order:
        raise NotImplementedError()

    def add(self, order: Order) -> None:
        raise NotImplementedError()


class PaymentProcessor:
    def process_payment(self, order_id: int, amount: float) -> bool:
        raise NotImplementedError()


class OrderProcessor:
    def __init__(self, order_repository: OrderRepository, payment_processor: PaymentProcessor) -> None:
        raise NotImplementedError()

    def execute(self, order_id: int) -> bool:
        raise NotImplementedError()
