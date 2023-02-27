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
        self.name_product = name_product
        self.price_product = price_product
        self.number_of_product = number_of_product
        self.all_product += (self, name_product, price_product, number_of_product)

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
