import copy


class Category:
    """Категория товаров"""
    name: str
    description: str
    products: list
    category_count: int = 0
    uniq_products_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = copy.deepcopy(products)
        Category.category_count += 1
        Category.uniq_products_count = len(set(products))
