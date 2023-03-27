import pytest
from eletronnics_store.utils.func import ProductPresentaion, Phone, KeyBoard


@pytest.fixture()
def item():
    item = ProductPresentaion("Смартфон", 10000, 20)
    return item


@pytest.fixture()
def file():
    path = 'test.csv'
    return path


@pytest.fixture()
def name():
    return ProductPresentaion.all_product


@pytest.fixture()
def phone():
    phone = Phone('iPhone 14', 120000, 5, 2)
    return phone


@pytest.fixture()
def keyboard():
    keyboard = KeyBoard('Dark Project KD87A', 9600, 5)
    return keyboard


@pytest.fixture()
def path_not_found():
    path_not_found = 'items.csv'
    return path_not_found


@pytest.fixture()
def path_error():
    path_error = 'items_error.csv'
    return path_error


def test_name_product(name):
    """
    Тест
    name_product
    """
    with pytest.raises(Exception):
        name.name_product = "Название не может быть длиннее 10 символов."


def test_from_csv(file, path_not_found, path_error):
    """
    Тест
    from_csv
    """
    ProductPresentaion.get_from_csv(file)
    assert len(ProductPresentaion.all_product) == 5
    assert ProductPresentaion.all_product[1].name_product == 'Ноутбук'
    with pytest.raises(FileNotFoundError, match='Отсутствует файл items.csv'):
        ProductPresentaion.get_from_csv(path_not_found)
    assert ProductPresentaion.get_from_csv(path_error) == print('Файл item.csv поврежден')


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
    ProductPresentaion.discount_price = 0.7
    assert item.get_discount_price() == 7000


def test_is_integer():
    """
    Тест
    is_integer
    """
    assert ProductPresentaion.is_integer(5) is True
    assert ProductPresentaion.is_integer(5.0) is True
    assert ProductPresentaion.is_integer(5.5) is False


def test_repr(item, phone):
    """
    Тест
    __repr__
    """
    assert item.__repr__() == "ProductPresentaion('Смартфон', '10000', 20)"
    assert phone.__repr__() == "Phone('iPhone 14', '120000', 5, 2)"


def test_str(item, phone):
    """
    Тест
    __str__
    """
    assert str(item) == "Смартфон"
    assert str(phone) == 'iPhone 14'


def test_add(item, phone):
    """
    Тест
    __add__
    """
    assert phone + item == 25
    with pytest.raises(ValueError, match='Складывать можно только объекты ProductPresentaion и Phone.'):
        phone + "10000"


def test_sim_cards(phone):
    """
    Тест
    sim_cards
    """
    phone.sim_cards = 0
    with pytest.raises(Exception):
        phone.sim_cards = "Количество физических SIM-карт должно быть целым числом больше нуля."


def test_change_lang(keyboard):
    """
    Тест
    change_lang
    """
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
