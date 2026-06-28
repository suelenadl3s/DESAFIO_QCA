class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity
    
    def __repr__(self):
        return f"name={self.name} | quantity={self.quantity} | price={self.price}"