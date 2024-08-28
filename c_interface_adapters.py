from b_use_cases import OrderProcessor


class OrderController:
    def __init__(self, order_processor: OrderProcessor) -> None:
        self.order_processor = order_processor

    def control_order(self, order_id: int) -> None:
        raise NotImplementedError()


class DummyOrderController(OrderController):
    def control_order(self, order_id: int) -> None:
        print(f"Processing order {order_id} on the dummy controller.")
        success = self.order_processor.execute(order_id)
        if success:
            print(f"Order {order_id} processed successfully.")
        else:
            print(f"Order {order_id} processing failed.")


class WebAPIOrderController(OrderController):
    def control_order(self, order_id: int) -> tuple:
        print(f"Processing order {order_id} on the web API.")
        success = self.order_processor.execute(order_id)
        if success:
            return (
                {"message": f"Order {order_id} processed successfully."},
                200,
            )
        else:
            return (
                {"message": f"Order {order_id} processing failed."},
                400,
            )
