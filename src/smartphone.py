from src.product import Product


class Smartphone(Product):
    model: str
    memory: int
    performance: str

    def __init__(self, name, description, price, count, color, model, memory, performance):
        super().__init__(name, description, price, count, color)
        self.model = model
        self.memory = memory
        self.performance = performance
