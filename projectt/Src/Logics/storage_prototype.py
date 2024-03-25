from Src.exceptions import argument_exception
from Src.errors import error_proxy
from Src.Models.storage_row_model import storage_row_model
from datetime import datetime
from Src.reference import reference
from Src.Models.storage_model import storage_model

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
    
    
    def filter_nomenclature(self, id: str):
        """
            Отфильтровать по номенклатуре (свойство транзакции)
        Args:
            id: str

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.nomenclature.id == id:
                result.append(item)

        return   storage_prototype( result )
    
    
    def filter_receipes(self, receipe: reference):
        """
            Отфильтровать данные по рецепту (номенклатуре рецепта)
        Args:
            receipe: reference

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data
        
        nomens = []
        for item in receipe.consist.values():
            nomens.append(item.nomenclature.id)

        result = []
        for item in self.__data:
            if item.nomenclature.id in nomens:
                result.append(item)
        
        return   storage_prototype( result )
    
    def filter_by_storage(self, storage: storage_model):
        """
            Отфильтровать данные по рецепту (по адрессу склада)
        Args:
            receipe: reference

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"


        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.storage.address == storage.address:
                result.append(item)  
    
    @property
    def data(self):
        return self.__data         
                
                   
            
            
        
    