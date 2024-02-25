from Src.exceptions import exception_proxy

#
# Класс для описания настроек
#
class settings():
    _inn = 0
    _short_name = ""
    __is_first_start = False
    
    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn
    
    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        self._inn = value
         
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self._short_name = value
            
    @property
    def is_first_start(self):
        return self.__is_first_start
    
    @is_first_start.setter
    def is_first_start(self, value: bool):
        if not isinstance(value, bool):
            pass

        self.__is_first_start = value
