import copy

from src.category import Category


class ProductIterator:
    """
    Принимает на вход категорию и дает возможность использовать цикл for
    для прохода по всем товарам данной категории.
    """
    __category: Category

    def __init__(self, category: Category):
        self.__category = copy.deepcopy(category)
        self.current = iter(self.__category.products)

    def __iter__(self):
        return self.current

    def __next__(self):
        return next(self.current)
