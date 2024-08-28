from b_use_cases import OrderProcessor


class OrderController:
    def __init__(self, order_processor: OrderProcessor):
        self.order_processor = order_processor

    def process_order(self, order_id):
        success = self.order_processor.execute(order_id)
        if success:
            print(f"Order {order_id} processed successfully.")
        else:
            print(f"Order {order_id} processing failed.")
