from a_entities import Item, Order
from c_interface_adapters import OrderController
from d_frameworks_and_drivers import (
    DummyOrderProcessor,
    UsdPaymentProcessor,
    InMemoryOrderRepository,
)


order_repository = InMemoryOrderRepository()
payment_processor = UsdPaymentProcessor()
order_processor = DummyOrderProcessor(order_repository, payment_processor)
order_controller = OrderController(order_processor)

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

# Processing the order
order_controller.process_order(1)
order_controller.process_order(2)
