from src.product import Product


class Grass(Product):
    origin_country: str
    germination_period: int

    def __init__(self, name, description, price, count, color, origin_country, germination_period):
        super().__init__(name, description, price, count, color)
        self.origin_country = origin_country
        self.germination_period = germination_period
