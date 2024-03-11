import os.path
from json import load

from category import Category
from product import Product


def load_categories(filepath=os.path.join('data', 'products.json')):
    with open(filepath) as file:
        json_list = load(file)
        categories = []
        for entity in json_list:
            products = []
            for product in entity.get('products', []):
                products.append(Product(product['name'], product['description'], float(product['price']),
                                        int(product['quantity'])))
            categories.append(Category(entity['name'], entity['description'], products))
    return categories
