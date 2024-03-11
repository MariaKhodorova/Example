from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference
from Src.Logics.convertor import convertor
from Src.Logics.reference_convertor import reference_convertor
import datetime


#
# Фабрика для конвертация данных во вложенный словарь
#
class convert_factory:
    
    def __init__(self):
        self.convertors = {
            int: basic_convertor(),
            str: basic_convertor(),
            bool: basic_convertor(),
            dict: basic_convertor(),
            datetime: datetime_convertor(),
        }
    
        
    def convert(self, object) -> dict:
        # Сконвертируем данные как список
        result = self.convert_list("data", object)
        if result is not None:
            return result
        
        result = {}
        fields = reference.create_fields(object)
        
        for field in fields:
            attribute = getattr(object.__class, field)
            if isinstance(attribute, property):
                value = getattr(object, field)
                
                # Сконвертируем данные как список
                dict =  self.__convert_list(field, value)
                if dict is None:
                    # Сконвертируем данные как значение
                    dict = self.__convert_item(field, value)
                    
                if len(dict) == 1:
                    result[field] =  dict[field]
                else:
                    result[field] = dict    
          
        return result  
    
    def __convert_item(self, field: str,  source):
        #Сконвертировать элемент
        if source is None:
            return {field: None}
        
        if type(source) not in self.convertors.keys():
            raise operation_exception(f"Не возможно подобрать конвертор для типа {type(source)}")

        convertor = self.convertors[type(source)]
        dict = convertor.convert(field, source)
        
        if not convertor.is_empty:
            raise operation_exception(f"Ошибка при конвертации данных {convertor.error}")
        
        return dict
            
    def __convert_list(self, field: str,  source) -> list:
        # Сконвертировать список
        if not isinstance(source, list):
            return None
        
        items = []
        for item in source:
            items.append(self.__convert_item(field, item))
        
        return items        