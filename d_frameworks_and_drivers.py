from b_use_cases import OrderProcessor, OrderRepository, PaymentProcessor


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def add(self, order):
        self.orders[order.order_id] = order


class DummyPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount}")
        return True  # Assume the payment is always successful for this example


class EurPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount} using Euro")
        return True  # Assume the payment is always successful for this example


class UsdPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount} using US Dollar")
        return True  # Assume the payment is always successful for this example


class DummyOrderProcessor(OrderProcessor):
    def __init__(
        self, order_repository: OrderRepository, payment_processor: PaymentProcessor
    ) -> None:
        self.order_repository = order_repository
        self.payment_processor = payment_processor

    def execute(self, order_id: int) -> bool:
        order = self.order_repository.get_order(order_id)
        total = order.calculate_total()

        if self.payment_processor.process_payment(order_id, total):
            order.status = "completed"
            self.order_repository.add(order)
            return True
        else:
            order.status = "failed"
            self.order_repository.add(order)
            return False
