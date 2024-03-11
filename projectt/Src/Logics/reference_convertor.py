from Src.Logics.convertor import convertor
from Src.reference import reference

# класс для формирования словаря по типу Reference

class reference_convertor(convertor):
    def convert(self, field: str, object) -> dict:
        super().convert( field, object)
      
        if not isinstance(object, object):
            self._error.error = f"Некорректный тип данных"
            return None
      
        try:
            return { field: object }
        except:
            self._error.set_error(Exception)  
            
     
