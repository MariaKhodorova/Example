from abc import ABC, abstractmethod
from Src.settings import settings
from Src.exceptions import exception_proxy, operation_exception
from Src.errors import error_proxy


#
# Абстрактный класс для конвертации
#
class convertor(error_proxy):
    
    @abstractmethod
    def convert(self, field: str, object) -> dict:
        # Данный метод возвращает словарь в формате ключ - наименование поля, значение - данные поля
        exception_proxy.validate(field, str)
        
        


