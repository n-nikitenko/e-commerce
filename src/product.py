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
