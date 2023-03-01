import pytest
from product.utils.func import ProductPresentaion


@pytest.fixture()
def item():
    item = ProductPresentaion("Смартфон", 10000, 20)
    return item


@pytest.fixture()
def name():
    return ProductPresentaion.all_product


def test_name_product(name):
    """
    Тест
    name_product
    """
    with pytest.raises(Exception):
        name.name_product = "Название не может быть длиннее 10 символов."


def test_from_csv():
    """
    Тест
    from_csv
    """
    ProductPresentaion.get_from_csv('test.csv')
    assert len(ProductPresentaion.all_product) == 5
    assert ProductPresentaion.all_product[1].name_product == 'Ноутбук'


def test_get_total_price_products(item):
    """
    Тест
    get_total_price_products
    """
    assert item.get_total_price_products() == 200000


def test_get_discount_price(item):
    """
    Тест
    get_discount_price
    """
    ProductPresentaion.discount_price = 0.8
    assert item.get_discount_price() == 8000


def test_is_integer():
    """
    Тест
    is_integer
    """
    assert ProductPresentaion.is_integer(5) is True
    assert ProductPresentaion.is_integer(5.0) is True
    assert ProductPresentaion.is_integer(5.5) is False
