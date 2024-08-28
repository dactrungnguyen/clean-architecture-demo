from b_use_cases import OrderProcessor


class OrderController:
    def __init__(self, order_processor: OrderProcessor) -> None:
        self.order_processor = order_processor

    def control_order(self, order_id: int) -> None:
        # TODO: add controller logic here
        self.order_processor.execute(order_id)
