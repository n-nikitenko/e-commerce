import copy


class Category:
    """Категория товаров"""
    name: str
    description: str
    products: list
    category_count: int = 0
    uniq_products_count: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = copy.deepcopy(products)
        Category.category_count += 1
        self.uniq_products_count = len(set(products))

    def __del__(self):
        Category.category_count -= 1
