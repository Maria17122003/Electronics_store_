import pytest
from eletronnics_store.utils.func import ProductPresentaion

# Создаем экземпляр класс Product_presentation
item1 = ProductPresentaion("Смартфон", 10000, 20)
ProductPresentaion.discount_price = 0.8


def test_get_total_price_products():
    """
    Тест
    get_total_price_products
    """
    assert item1.get_total_price_products() == 200000


def test_get_discount_price():
    """
    Тест
    get_discount_price
    """
    assert item1.get_discount_price() == 8000
