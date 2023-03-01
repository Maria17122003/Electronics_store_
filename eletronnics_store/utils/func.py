import csv


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
        экземпляры класса
        """
        with open(path) as file:
            file_csv = csv.DictReader(file)
            for item in file_csv:
                cls(
                    name_product=item['name'],
                    price_product=float(item['price']),
                    number_of_product=int(item['quantity'])
                )

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
