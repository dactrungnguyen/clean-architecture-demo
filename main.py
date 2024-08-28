from flask import Flask, jsonify

from a_entities import Item, Order
from c_interface_adapters import DummyOrderController, WebAPIOrderController
from d_frameworks_and_drivers import (
    DummyOrderProcessor,
    UsdPaymentProcessor,
    InMemoryOrderRepository,
)


order_repository = InMemoryOrderRepository()
payment_processor = UsdPaymentProcessor()
order_processor = DummyOrderProcessor(order_repository, payment_processor)
dummy_order_controller = DummyOrderController(order_processor)
web_api_order_controller = WebAPIOrderController(order_processor)

# Adding an order to the repository
order_repository.add(
    Order(
        1,
        [
            Item(name="Item 1", price=10, quantity=2, currency="USD"),
            Item(name="Item 2", price=5, quantity=1, currency="USD"),
        ],
    )
)
order_repository.add(
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
    return web_api_order_controller.control_order(order_id)


if __name__ == "__main__":
    # using the dummy controller
    # order_id = int(input("Enter order ID: "))
    # dummy_order_controller.control_order(order_id)
    # using the Web controller
    app.run(debug=True)
