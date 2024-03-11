from Src.Logics.Reporting import Reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception, operation_exception

#фабрика для отчетов
class report_factory:
    _maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        #создать структуру
        self.__maps["csv"] = csv_reporting
        self.__maps["markdown"] = markdown_reporting

    
    def create(self, format: str, data) -> Reporting:

        #Сформировать объект отчет
        exception_proxy.validate(format, str)
        if data is None:
            raise argument_exception("Данные не...")
        
        if len(data) == 0:
            raise argument_exception("Данные пустые")
        
        if format not in self.__maps.keys():
            raise operation_exception(f"Для{format}...")
        
        report_type = self.__maps(format)

        result = report_type(data)

        return data
        

            
