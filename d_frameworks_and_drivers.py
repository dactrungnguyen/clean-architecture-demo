from flask import Flask, jsonify
from a_entities import Item, Order
from b_use_cases import OrderRepository, PaymentProcessor, OrderProcessor
from c_interface_adapters import OrderController


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def update_order(self, order):
        self.orders[order.order_id] = order


class EurPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount} using Euro")
        return True  # Assume the payment is always successful for this example


class UsdPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount} using US Dollar")
        return True  # Assume the payment is always successful for this example


class DummyPaymentProcessor(PaymentProcessor):
    def process_payment(self, order_id: int, amount: float) -> bool:
        print(f"Processing payment for order {order_id}: ${amount}")
        return True  # Assume the payment is always successful for this example


order_repository = InMemoryOrderRepository()
payment_processor = UsdPaymentProcessor()
order_processor = OrderProcessor(order_repository, payment_processor)
order_controller = OrderController(order_processor)

# Adding orders to the repository
order_repository.update_order(
    Order(
        1,
        [
            Item(name="Item 1", price=10, quantity=2, currency="USD"),
            Item(name="Item 2", price=5, quantity=1, currency="USD"),
        ],
    )
)
order_repository.update_order(
    Order(
        2,
        [
            Item(name="Item 3", price=20, quantity=1, currency="EUR"),
        ],
    )
)


app = Flask(__name__)


@app.route("/orders/<int:order_id>/process", methods=["POST"])
def control_order_route(order_id: int) -> tuple:
    success = order_controller.control_order(order_id)
    if success:
        return jsonify({"message": f"Order {order_id} processed successfully."}), 200
    else:
        return jsonify({"message": f"Order {order_id} processing failed."}), 400


if __name__ == "__main__":
    # app.run(debug=True)
    order_id = 1
    order_controller.control_order(order_id)
    order_id = 2
    order_controller.control_order(order_id)
    order_id = 1
    order_controller.control_order(order_id)
