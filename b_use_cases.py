from a_entities import Order


class OrderRepository:
    def get_order(self, order_id: int) -> Order:
        raise NotImplementedError()

    def update_order(self, order: Order) -> None:
        raise NotImplementedError()


class PaymentProcessor:
    def process_payment(self, order_id: int, amount: float) -> bool:
        raise NotImplementedError()


class OrderProcessor:
    def __init__(
        self, order_repository: OrderRepository, payment_processor: PaymentProcessor
    ) -> None:
        self.order_repository = order_repository
        self.payment_processor = payment_processor

    def execute(self, order_id: int) -> bool:
        order = self.order_repository.get_order(order_id)
        # check order status
        if order.status != "pending":
            print(f"Order {order_id} is not pending, processing failed.")
            return False

        # process payment
        total = order.calculate_total()
        if self.payment_processor.process_payment(order_id, total):
            order.status = "completed"
            self.order_repository.update_order(order)
            print(f"Order {order_id} processed successfully.")
            return True
        else:
            order.status = "failed"
            self.order_repository.update_order(order)
            print(f"Order {order_id} processing failed.")
            return False
