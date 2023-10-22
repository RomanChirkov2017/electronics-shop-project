"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError

def test_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.calculate_total_price() == 200000

def test_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item1 = Item('Смартфон', 10000.0, 20)
    assert repr(item1) == Item('Смартфон', 10000.0, 20)

def test_str():
    item1 = Item('Смартфон', 10000.0, 20)
    assert str(item1) == 'Смартфон'

def test_from_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match='Отсутствует файл items.csv'):
        Item.instantiate_from_csv()

def test_from_crashed_csv():
    with pytest.raises(InstantiateCSVError, match='Файл items.csv поврежден'):
        Item.instantiate_from_csv()
