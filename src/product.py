class Product:
    """Товар"""
    name: str
    description: str
    price: float
    count: int

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.price = price
        self.count = count

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, count={self.count})"
