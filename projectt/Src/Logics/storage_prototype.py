from Src.exceptions import argument_exception
from Src.errors import error_proxy
from datetime import datetime


#
# Прототип для обработки складских транзакций
#
class storage_prototype(error_proxy):
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error = "Некорректно переданы параметры!"
        
        self.__data = data

    def filter( self,start_period: datetime, stop_period: datetime  ):
        """
            Отфильтровать по периоду
        Args:
            data (list): список складских транзакций
            start_period (datetime): начало
            stop_period (datetime): окончание

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"
            
        if start_period > stop_period:
            self.error = "Некорректный период!"
            
         
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)
                
        return   storage_prototype( result )
    
    
    def filter_nomenclature(self, nomenclature_id):
        """
            Отфильтровать по номенклатуре
        Args:
            nomenclature_id: id номенклатуры

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.nomenclature_id == nomenclature_id:
                result.append(item)

        return   storage_prototype( result )
    
    
    def filter_receipes(self, receipe_id):
        """
            Отфильтровать данные по рецепту
        Args:
            receipe_id: str 

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.storage_key == receipe_id:
                result.append(item)

        return   storage_prototype( result )
    
    
    @property
    def data(self):
        return self.__data         
                
                   
            
            
        
    