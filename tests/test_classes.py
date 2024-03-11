import pytest

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
def smartphones(samsung_galaxy, iphone_15):
    return [samsung_galaxy, iphone_15]


@pytest.fixture
def smartphones_category(smartphones):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации,"
                    " но и получение дополнительных функций для удобства жизни",
                    smartphones)


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
