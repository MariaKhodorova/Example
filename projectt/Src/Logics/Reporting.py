from Src.Storage.storage import storage
from abc import ABC, abstractmethod
from Src.settings import settings

#
# Абстрактный класс для наследования
#
class Reporting(ABC):
    storage = None
    def __init__(self, storage: storage):
        self.storage = storage 

    @abstractmethod
    def create(self,skey):
        return ""

    