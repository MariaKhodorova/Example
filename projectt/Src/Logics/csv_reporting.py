from Src.Storage.storage import storage
from Src.Logics.Reporting import Reporting
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model
from Src.Models.receipe_row_model import receipe_row_model
from Src.Models.unit_model import unit_model
from Src.exceptions import operation_exception

class csv_reporting(Reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = ""
        delimetr = ";"

        # Исходные данные
        items = self.data[ typeKey ]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        # Заголовок 
        header = delimetr.join(self.fields)
        result += f"{header}\n"
        
        # Данные
        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""
                    
                row +=f"{value}{delimetr}"
                
            result += f"{row[:-1]}\n"
            
        
        # Результат csv
        return result