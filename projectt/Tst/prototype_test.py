from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
import unittest
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from datetime import datetime
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model

class prototype_test(unittest.TestCase):
    
    
    def test_check_prototype(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype( data )
        
        
        # Дейтсвие
        result = prototype.filter(   start_date, stop_date ) 
        
        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty

    def test_check_filter_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        nomenclature = nomenclature_model()
        prototype = storage_prototype( data )

        # Действие
        result = prototype.filter_nomenclature( nomenclature )

        # Проверка
        assert isinstance(result, nomenclature_model)

    def test_check_filter_receipes(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        receipe = receipe_model()
        prototype = storage_prototype( data )

        # Действие
        result = prototype.filter_receipes( receipe )

        # Проверка
        assert isinstance(result, receipe_model)
    