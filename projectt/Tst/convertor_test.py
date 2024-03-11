
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.convertor import convertor
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.reference_convertor import reference_convertor
from Src.Logics.convert_factory import convert_factory

import unittest
import datetime

#
# Набор автотестов для проверки конвертиции
#
class convert_test(unittest.TestCase):
    def test_reference_convertor(self):
        # Подготовка
        convertor = reference_convertor()
        input_obj = object()

        # Действие
        result = convertor.convert('field', input_obj)

        # Проверка
        self.assertEqual(result, {'field': input_obj})
        self.assertIsNone(result)


    def test_basic_convertor(self):
        # Подготовка
        convertor = basic_convertor()
        valid_types = []

        # Действие
        result = convertor.convert('field', valid_types)
            
        # Проверка
        self.assertEqual(result, {'field': valid_types})
        self.assertIsNone(result)


    def test_datetime_convertor(self):
        # Подготовка
        convertor = datetime_convertor()
        input_obj = datetime.now()
        error = 'invalid'

        # Действие
        result = convertor.convert('field', input_obj)

        # Проверка
        self.assertIsInstance(result, dict)
        self.assertIsNone(error)


    def test_convert_factory(self):
        # Подготовка
        factory = convert_factory()
        input_obj = {'key': 'value'}

        # Действие
        result = factory.convert(input_obj)

        # Проверка
        self.assertEqual(result, {'key': 'value'})
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
