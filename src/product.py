class Product:
    """Товар"""
    name: str
    description: str
    __price: float
    count: int

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.__price = price
        self.count = count

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, count={self.count})"

    @classmethod
    def create_product(cls, name, description, price, count, category):
        """Проверяет наличие схожего товара в категории и возвращает созданный товар"""
        duplicates = [p for p in category.products if p.name.lower() == name.lower()]
        for p in duplicates:
            count += p.count
            price = max(price, p.price)
        return cls(name, description, price, count)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        '''Устанавливает новое значение цены, если оно больше нуля. Если цена понижается, запрашивается подтверждение
        пользователя'''
        if value <= 0:
            print("Значение цены должно быть больше нуля")
            return
        if value < self.__price:
            user_answer = input("Вы уверены, что хотите понизить цену? Введите y/n")
            if user_answer.lower() != 'y':
                return
        self.__price = value
