class Invoice:
    def __init__(self, order_id: str, date: str, customer_id: str, products: list):
        self.order_id = order_id
        self.date = date
        self.customer_id = customer_id
        self.products = products

    def total_value(self):
        return sum(p.total() for p in self.products)