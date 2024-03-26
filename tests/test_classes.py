import pytest

from src.grass import Grass
from src.product_interator import ProductIterator
from src.category import Category
from src.product import Product


@pytest.fixture
def samsung_galaxy():
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def iphone_15():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def iphone_15_duplicate():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def grass():
    return Grass("Grass", "green", 10000.0, 10, "green", "USA", 14)


@pytest.fixture
def smartphones(samsung_galaxy, iphone_15):
    return [samsung_galaxy, iphone_15]


@pytest.fixture
def smartphones_category(smartphones):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации,"
                    " но и получение дополнительных функций для удобства жизни",
                    smartphones)


@pytest.fixture
def not_product():
    class NotProduct:
        def __init__(self, name, description, price, count):
            self.name = name
            self.description = description
            self.price = price
            self.count = count

    return NotProduct("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


def test_category(smartphones_category):
    assert smartphones_category.name == "Смартфоны"
    assert smartphones_category.description == ("Смартфоны, как средство не только коммуникации,"
                                                " но и получение дополнительных функций для удобства жизни")


def test_category_uniq_products_count(smartphones_category):
    assert smartphones_category.uniq_products_count == len(set(smartphones_category.products))


def test_category_count(smartphones_category):
    assert smartphones_category.category_count == 1


def test_product(iphone_15):
    assert iphone_15.name == "Iphone 15"
    assert iphone_15.description == "512GB, Gray space"
    assert iphone_15.price == 210000.0
    assert iphone_15.count == 8


def test_add_product(smartphones_category, iphone_15_duplicate):
    category_len = len(smartphones_category.products)
    smartphones_category.add_product(iphone_15_duplicate)
    assert len(smartphones_category.products) == category_len


def test_add_not_product(smartphones_category, iphone_15_duplicate, not_product, grass):
    """При добавлении в категорию продукта, который не является экземпляром класса Product или его наследников
    должно возникнуть исключение ValueError"""
    try:
        len_category = len(smartphones_category)
        smartphones_category.add_product(grass)
        assert len_category + len(grass) == len(smartphones_category)
        smartphones_category.add_product(not_product)
        assert False
    except ValueError:
        assert True


def test_set_zero_price(iphone_15):
    iphone_15.price = 0
    assert iphone_15.price != 0


def test_products_sum(iphone_15, samsung_galaxy, grass):
    assert iphone_15 + samsung_galaxy == iphone_15.price * iphone_15.count + samsung_galaxy.price * samsung_galaxy.count
    try:
        samsung_galaxy + grass  # должно возникнуть исключение TypeError
        assert False
    except TypeError:
        assert True


def test_product_iterator(smartphones_category):
    products = ProductIterator(smartphones_category)
    is_empty = False
    while not is_empty:
        try:
            p = next(products)
            assert isinstance(p, Product)
        except StopIteration:
            is_empty = True
            assert True
    assert len(list(ProductIterator(smartphones_category))) == len(smartphones_category.products)
