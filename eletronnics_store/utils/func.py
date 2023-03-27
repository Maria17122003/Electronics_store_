import csv
import os.path


class InstantiateCSVError(Exception):
    """Класс исключение для ошибок,
     связанных с пореждением файла"""
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл Items.csv поврежден'

    def __str__(self):
        return self.message


class ProductPresentaion:
    discount_price = 1
    all_product = []

    def __init__(self, name_product, price_product, number_of_product):
        """
        Создаем атрибуты
        название товара,
        цена за единицу товара,
        количество товара в магазине
        """
        self.__name_product = name_product
        self.price_product = price_product
        self.number_of_product = number_of_product
        self.all_product.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name_product}', '{self.price_product}', {self.number_of_product})"

    def __str__(self):
        return f'{self.__name_product}'

    @property
    def name_product(self) -> str:
        return self.__name_product

    @name_product.setter
    def name_product(self, name_product):
        if len(name_product) > 10:
            raise ValueError("Название не может быть длиннее 10 символов.")
        self.__name_product = name_product

    def get_total_price_products(self):
        """
        Возвращает
        общую стоимость
        конкретного товара
        """
        price = self.price_product * self.number_of_product
        return price

    def get_discount_price(self):
        """
        Возвращает
        стоимость товара со
        скидкой
        """
        self.price_product = self.price_product * self.discount_price
        return self.price_product

    @classmethod
    def get_from_csv(cls, path: str):
        """
        Считывает данные
        из csv-файла
        и создает
        экземпляры класса,
        выбрасывает исключение если файл не найден
        или поврежден
        """
        if not os.path.isfile(path):
            raise FileNotFoundError('Отсутствует файл items.csv')

        with open(path) as file:
            try:
                file_csv = csv.DictReader(file)
                for item in file_csv:
                    if list(item.keys()) == ['name', 'price', 'quantity']:
                        cls(
                            name_product=item['name'],
                            price_product=float(item['price']),
                            number_of_product=int(item['quantity'])
                            )
                    else:
                        raise InstantiateCSVError
            except InstantiateCSVError:
                print(InstantiateCSVError('Файл item.csv поврежден'))

    @staticmethod
    def is_integer(num) -> bool:
        """
        Проверяет
        является ли
        число целым
        """
        if isinstance(num, int) or isinstance(num, float) and num % 1 == 0:
            return True
        return False


class Phone(ProductPresentaion):
    def __init__(self, name_product, price_product, number_of_product, sim_cards):
        """
        Создаем новый атрибут
        количество сим карт
        """
        super().__init__(name_product, price_product, number_of_product)
        self.sim_cards = sim_cards

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name_product}', '{self.price_product}', " \
               f"{self.number_of_product}, {self.__sim_cards})"

    def __str__(self):
        return f'{self.name_product}'

    def __add__(self, other):
        """
        Складывает количество
        товаров в магазине
        """
        if not isinstance(other, ProductPresentaion):
            raise ValueError('Складывать можно только объекты ProductPresentaion и Phone.')
        return int(self.number_of_product) + int(other.number_of_product)

    @property
    def sim_cards(self) -> int:
        return self.__sim_cards

    @sim_cards.setter
    def sim_cards(self, sim_cards):
        if sim_cards < 0 and isinstance(sim_cards, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__sim_cards = sim_cards


class MixinLog:
    """
    Класс
    MixinLog,
    который дополняет
    KeyBoard
    """

    def __init__(self, language):
        super().__init__()
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """
        Меняет язык на
        русский
        """
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"


class KeyBoard(ProductPresentaion, MixinLog):
    def __init__(self, name_product, price_product, number_of_product, language="EN"):
        """
        Создаем новый атрибут
        язык
        """
        super().__init__(name_product, price_product, number_of_product)
        self._language = language
