import copy


class Category:
    """Категория товаров"""
    name: str
    description: str
    __products: list
    category_count: int = 0
    uniq_products_count: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        for p in products:
            self.add_product(copy.deepcopy(p))
        Category.category_count += 1
        self.uniq_products_count = len(set(products))

    def __del__(self):
        Category.category_count -= 1

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}', products={self.__products})"

    def add_product(self, product):
        '''Добавляет товар в список товаров категории
        Если в списке товаров уже есть такой товар, суммируется количество и устанавливается максимальная цена'''
        duplicates = [p for p in self.__products if p.name.lower() == product.name.lower()]
        for p in duplicates:
            product.count += p.count
            product.price = max(product.price, p.price)
            self.__products.remove(p)
        self.__products.append(product)

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.count} шт.")
        return self.__products
