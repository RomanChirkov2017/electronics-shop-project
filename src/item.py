from csv import DictReader

from settings import ITEMS_CSV_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_csv_path = ITEMS_CSV_PATH

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(cls.items_csv_path, 'r', encoding='windows-1251') as csv:
            reader = DictReader(csv)
            for row in reader:
                cls(
                    name=row['name'],
                    price=cls.string_to_number(row['price']),
                    quantity=cls.string_to_number(row['quantity'])
                )

    @staticmethod
    def string_to_number(number_string: str):
        return int(float(number_string))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate
        return self.price
