from Src.Logics.convertor import convertor
import datetime


# класс для формирования словаря по типу DateTime 
class datetime_convertor(convertor):
    
    def convert(self, field: str,  object):
        super().convert( field, object)
      
        if not isinstance(object, datetime):
          self._error.error = f"некорректный тип данных"
          return 
      
        try:
            return { field: object.strftime('%YYYY-%mm-%dd %HH:%ss') }
        except:
            self.set_error(Exception) 
