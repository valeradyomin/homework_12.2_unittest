import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        # тест с пустым списком
        self.assertEqual(arrs.my_slice([], 0, 2), [])
        # тест с отрицательным индексом старта
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])
        # тест с отрицательным индексом конца
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, -1), [2, 3])
        # тест с индексом начала выходящим за пределы списка
        self.assertEqual(arrs.my_slice([1, 2, 3], 10), [])
        # тест с индексом конца выходящим за пределы списка
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 10), [2, 3])
        # тест с отрицательным индексом начала выходящим за пределы списка
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -7), [1, 2, 3, 4, 5])
