from Src.Logics.convertor import convertor


# класс для формирования словаря по простым типам
class basic_convertor(convertor):
   
   def convert(self, field: str, object) -> dict:
        super().convert( field, object)
      
        if not isinstance(object, (int, str, bool)):
            self._error.error = f"Некорректный тип данных"
            return None
      
        try:
            return { field: object }
        except:
            self._error.set_error(Exception)  
            
  

   
   

        


